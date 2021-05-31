from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import EducationForm, ExperieceForm

from myapp.models import Profile, Experience, Education, KeySkill




def template2(request):
    return render(request, 'template2.html')


class Create_CV(ListView):
    model = Profile
    template_name = "template1.html"
    
class AddEducationView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'add_education.html'
    
    def form_valid(self, form):
        form.instance.user_id = self.kwargs['pk']  
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
    
    

    
class AddExperienceView(CreateView):
    model = Experience
    form_class = ExperieceForm
    template_name = "add_experience.html"
     
    def form_valid(self, form):
        form.instance.user_id = self.kwargs['pk']  
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')
    
class AddSkillsView(CreateView):
    model = KeySkill
    template_name = "add_skills.html"
    fields = ["skill"]
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        form.instance.user_id = self.kwargs['pk']  
        return super().form_valid(form)
    
    
    