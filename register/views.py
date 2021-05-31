from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm ,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from myapp.models import Profile



def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f'Account created for {username}!')
            return redirect("/login")
    else:
        form = RegisterForm()
        
    return render(response, 'registration/register.html', {"form":form})

class UserEditView(generic.UpdateView):
    form_class = ProfileForm
    template_name = "registration/profile_settings.html"
    success_url = reverse_lazy('profile')
    
    
    def get_object(self):
        return self.request.user
    

class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('profile')
    
class CreateProfilePageView(generic.CreateView):
    model = Profile
    template_name ="registration/create_user_profile.html"
    success_url = reverse_lazy('home')
    fields = ['bio','profile_pic', 'website', 'facebook', 'linkedin', 'instagram', 'twitter']
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user   
        return super().form_valid(form)
    
    
    