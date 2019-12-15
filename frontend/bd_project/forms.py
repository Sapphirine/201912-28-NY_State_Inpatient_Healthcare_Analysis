from django import forms
from .variables import *

class QueryForm(forms.Form):

    field1_choice = forms.CharField(label='Select your first field', widget=forms.Select(choices=FIELD1_CHOICES))
    field2_choice = forms.CharField(label='Select your second field', widget=forms.Select(choices=FIELD2_CHOICES))

class PredictionForm(forms.Form):
    field1_choice = forms.CharField(label="Zip Code (3 Digits)", widget=forms.Select(choices=ZIP_CODES))
    field2_choice = forms.CharField(label="Age Group", widget=forms.Select(choices=AGE_GROUP))
    field3_choice = forms.CharField(label="Gender", widget=forms.Select(choices=GENDER))
    field4_choice = forms.CharField(label="Race", widget=forms.Select(choices=RACE_GROUP))
    field5_choice = forms.CharField(label="Type of Admission", widget=forms.Select(choices=TYPE_OF_ADMISSION))

class HeatMapForm(forms.Form):
    field1_choice = forms.CharField(label="Diagnosis", widget=forms.Select(choices=DIAGNOSIS_TYPES))
    field2_choice = forms.CharField(label="Category", widget=forms.Select(choices=CATEGORY_CHOICES))
    field3_choice = forms.CharField(label="Group 1", widget=forms.Select(choices=[(None,'-----')]))
    field4_choice = forms.CharField(label="Group 2", widget=forms.Select(choices=[(None,'-----')]))
