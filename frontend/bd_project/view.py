import os
import time
import math
import json
import pandas_gbq
from collections import OrderedDict
from google.cloud import storage
from google.oauth2 import service_account
from django.http import HttpResponse
from django.shortcuts import render
from .forms import QueryForm, PredictionForm, HeatMapForm 
from .variables import AGE_GROUP, RACE_GROUP, GENDER, ETHNICITY_GROUP
# Make sure you have installed pandas-gbq at first;
# You can use the other way to query BigQuery.
# please have a look at
# https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-nodejs
# To get your credential

credentials = service_account.Credentials.from_service_account_file('./big-data-project-3e775fe96b07.json')

HEATMAP_CHOICE = {
    'Race' : [{'value': k, 'label': v} for k, v in RACE_GROUP],
    'Age_Group' : [{'value': k, 'label': v} for k, v in AGE_GROUP],
    'Gender' : [{'value': k, 'label': v} for k, v in GENDER],
    'Ethnicity' : [{'value': k, 'label': v} for k, v in ETHNICITY_GROUP],
    '-----' : []
}


def hello(request):
    context = {}
    context['content1'] = 'Hello World!'
    return render(request, 'helloworld.html', context)

def home(request):
    context = {}
    context['content1'] = 'Hello World!'
    return render(request, 'home.html', context)

def dashboard(request):
    
    if request.method == "POST":
        
        form = QueryForm(request.POST)

        if form.is_valid():
            field1 = form.cleaned_data['field1_choice'] # field1
            field2 = form.cleaned_data['field2_choice'] # field2

        pandas_gbq.context.credentials = credentials
        pandas_gbq.context.project = "big-data-project-259618"

        SQL = """
        SELECT {field1} as field1, {field2} as field2, count(*) as group_count
        FROM `big-data-project-259618.dataset.sparcs2017`
        GROUP BY {field1}, {field2}
        ORDER BY {field1}, {field2} DESC
        """.format(field1 = field1, field2= field2)

        df = pandas_gbq.read_gbq(SQL)

        # Format of data:
        # {'data': [{'Age_Group': '0-17', 'gender': {'U': xxx, 'M': xxx, 'F': xxx}},
        #            {'Age_Group': '18-34', 'gender': {'U': xxx, 'M': xxx, 'F': xxx}}, ...],
        #  'name': ['Age_Group', 'Gender'],
        #  'field1_category': set("0-17"....),
        #  'field2_category': set("U", "M", "F")}

        data = dict()
        data['name'] = [field1, field2]
        data['field1_category'] = set()
        data['field2_category'] = set()
        data['data'] = []

        temp = {}
        curr_group = None
        
        for idx, row in df.iterrows():
            data['field1_category'].add(row['field1'])
            data['field2_category'].add(row['field2'])

            curr_group = row['field1']
            if curr_group not in temp.values():
                if temp:
                    data['data'].append(temp)
                    temp = {field1: curr_group, field2: OrderedDict()}
                    
                else:
                    temp[field1] = curr_group 
                    temp[field2] = OrderedDict()

            temp[field2][row['field2']] = row['group_count']

        data['data'].append(temp)

        data['field1_category'] = sorted(list(data['field1_category']))
        data['field2_category'] = sorted(list(data['field2_category']))
    
        for d in data['data']:
            for cat in data['field2_category']:
                if cat not in d[field2].keys():
                    d[field2][cat] = 0
            d[field2] = dict(sorted(d[field2].items()))

        return render(request, 'dashboard.html', {"data" : data, "form" : QueryForm()})
    else:
        return render(request, 'dashboard.html', {"form" : QueryForm()})

def prediction(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)

        if form.is_valid():
            field1 = form.cleaned_data['field1_choice'] # zip code
            field2 = form.cleaned_data['field2_choice'] # age group
            field3 = form.cleaned_data['field3_choice'] # gender
            field4 = form.cleaned_data['field4_choice'] # race
            field5 = form.cleaned_data['field5_choice'] # type of admission
            
            # submit user data to process and predict cost in Spark Cluster
            os.system("gcloud dataproc jobs submit pyspark \
                      --cluster project-cluster gs://final-project-1/sparkJob.py -- --age '{}' --zipcode '{}' --gender '{}' --toa '{}' --race '{}'".format(field2, field1, field3, field5, field4))

            print ('Finished Spark Job...')

            # retrieve results from GCP bucket
            os.system("gsutil -m cp -R gs://final-project-1/output.txt .")
            with open("output.txt", 'r') as f:
                for line in f:
                    prediction = line

            # regular SQL query
            pandas_gbq.context.credentials = credentials
            pandas_gbq.context.project = "big-data-project-259618"

            SQL = """
            SELECT AVG(Total_Charges/Length_of_Stay) as avg_total_charges_per_day
            FROM `big-data-project-259618.dataset.sparcs2017`
            WHERE Zip_Code___3_digits = "{zip}" AND Age_Group = "{age}" AND \
            Gender = "{gender}" AND Race = "{race}" AND Type_of_Admission = "{type_of_admission}"
            """.format(zip=field1, age=field2, gender=field3, race=field4, type_of_admission=field5)

            print ('Finished SQL Job...')

            df = pandas_gbq.read_gbq(SQL)
            cost = round(df.iloc[0]['avg_total_charges_per_day'], 2)

            data = [str(cost), str(round(float(prediction), 2))] # get predicted cost

    elif request.method == "GET":
        form = PredictionForm()
        data = None

    return render(request, 'prediction.html', {"data": data, "form" : form})

def heatmap(request):

    if request.method == "POST":
        form = HeatMapForm(request.POST)
        if form.is_valid():
            diagnosis = form.cleaned_data['field1_choice'] # Diagnosis
            category = form.cleaned_data['field2_choice'] # Category
            group1 = form.cleaned_data['field3_choice'] # Group 1
            group2 = form.cleaned_data['field4_choice'] # Group 2

        # run sql query
        pandas_gbq.context.credentials = credentials
        pandas_gbq.context.project = "big-data-project-259618"

        SQL = """
        SELECT Hospital_County,  AVG(case when {category} = "{group1}" then Total_Charges/Length_of_Stay else NULL end) as avg_total_charges_per_day_g1,
                                 AVG(case when {category} = "{group2}" then Total_Charges/Length_of_Stay else NULL end) as avg_total_charges_per_day_g2
        FROM `big-data-project-259618.dataset.sparcs2017`
        WHERE CCS_Diagnosis_Description = "{diagnosis}"
        GROUP BY Hospital_County
        ORDER BY Hospital_County ASC
        """.format(diagnosis=diagnosis, category=category, group1=group1, group2=group2)

        df = pandas_gbq.read_gbq(SQL)

        # calculate group1 column - group2 column
        df['delta'] = df['avg_total_charges_per_day_g1'] - df['avg_total_charges_per_day_g2']
        df.drop(['avg_total_charges_per_day_g1', 'avg_total_charges_per_day_g2'], axis=1)
        
        #formulate data object
        data = {}
        for index, row in df.iterrows():
            if not math.isnan(row['delta']):
                data[row['Hospital_County']] = row['delta']

        print (data)

    elif request.method == "GET":
        form = HeatMapForm()
        data = None
    with open('ny-topojson.json', 'r') as f:
        obj = f.read()

    return render(request, 'heatmap.html', {"data": data, "form" : form, "topology" : json.loads(obj)})

def load_dependents(request):
    category = request.GET.get('category')
    print(category)
    options = HEATMAP_CHOICE[category]

    return render(request, 'temp/group_dropdown_list_options.html', {'options': options})
