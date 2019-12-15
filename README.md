# nyhealth-bigdata

1) To run our web app use the following code to run a local host instance:
```
cd frontend/bd_project
python3 manage.py runserver
```
Then go to 127.0.0.1/PORT/home.html to access the app.

**Note that you may need to set up data tables in BigQuery with proper credentials and GCP Dataproc clusters set up before being able to use all features of the webapp.**

2) All the code for data exploration is in the "data_exploration" folder. Code for visualization and prediction model training is in the "code" folder. Finally, the bias analysis is contained in the "bias" folder.

3) Source data is from the All the codes for the analysis are in the folder called "Backend.zip". Datasets used are in the dataset folder inside the "Backend.zip".
