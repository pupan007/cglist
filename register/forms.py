from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from myapp.models import Profile




class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField( max_length=255, required=True)
    last_name = forms.CharField( max_length=255, required=True)
    birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years =[x for x in range(1920, 2021)]))
    
    class Meta:
        model = User
        fields =["username","first_name","last_name","email", 'password1', "password2"]
        


class ProfileForm(UserChangeForm):
    adress = forms.CharField(max_length=255)
    
    
    class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name', 'email','password']
         

# class ProfilePageForm(forms.ModelForm):
#     model = Profile
#     fields = ('bio', 'profile_pic', 'website', 'facebook', 'linkedin', 'instagram', 'twitter')
    
#     widgets = {
        
#     }
    
    
    
    
    
#     bio = models.TextField()
#     profile_pic = models.ImageField(null = True, blank = True,  upload_to = "images/profile/")
#     website  = models.CharField(max_length = 255, null= True, blank = True)
#     facebook = models.CharField(max_length = 255, null= True, blank = True)
#     linkedin = models.CharField(max_length = 255, null= True, blank = True)
#     instagram = models.CharField(max_length = 255, null= True, blank = True)
#     twitter = models.CharField(max_length = 255, null= True, blank = True)
    