from django import forms
from django.forms import SelectDateWidget
from myapp.models import Education, Experience


import datetime




    
class EducationForm(forms.ModelForm):  
    class Meta:
        model = Education
        fields = ['school_name', 'description' ,'start_date', 'end_date']
        widgets = {
            'start_date' :SelectDateWidget(years = range(1950 ,datetime.date.today().year + 1)),
            'end_date': SelectDateWidget(years = range(1950 ,datetime.date.today().year + 1))
        }
        
class ExperieceForm(forms.ModelForm):  
    class Meta:
        model = Experience
        fields = ['job_name', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date' :SelectDateWidget(years = range(1950 ,datetime.date.today().year + 1)),
            'end_date': SelectDateWidget(years = range(1950 ,datetime.date.today().year + 1))
        }
        

