from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.forms import SelectDateWidget


class Post(models.Model):
    title = models.CharField(max_length = 255)
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank = True, null = True)
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    
    def total_likes(self):
        return self.likes.count() 
    
      
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    
    def get_absolute_url(self):
        return reverse("detailed_view", kwargs={"pk": self.pk}) 
    
    

        

class Profile(models.Model):
    user  = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True,  upload_to = "images/profile/")
    website  = models.CharField(max_length = 255, null= True, blank = True)
    facebook = models.CharField(max_length = 255, null= True, blank = True)
    linkedin = models.CharField(max_length = 255, null= True, blank = True)
    instagram = models.CharField(max_length = 255, null= True, blank = True)
    twitter = models.CharField(max_length = 255, null= True, blank = True)
    phone = models.CharField(max_length = 255, null= True, blank = True)
    github = models.CharField(max_length = 255, null= True, blank = True)
    
    
    
       
    def __str__(self):
        return str(self.user)
    
class Experience(models.Model):
    user = models.ForeignKey(Profile, related_name="experience", null= True, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=255,null= True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True)
    end_date = models.DateField( auto_now=False, auto_now_add=False, null = True, blank = True)
    name = models.CharField(max_length=255,null= True,)
    description = models.TextField(max_length=500,null= True)
    
    
    def get_absolute_url(self):
        return reverse("add_experience", kwargs={"id": self.id}) 
    
    def __str__(self):
        return self.job_name
    
    
class Education(models.Model):
    user = models.ForeignKey(Profile, related_name="education", null= True, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255,null= True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True,)
    end_date = models.DateField( auto_now=False, auto_now_add=False, null = True, blank = True)
    description = models.TextField(max_length=500,null= True)
    
    def get_absolute_url(self):
        return reverse("add_education", kwargs={"id": self.id}) 
    
    def __str__(self):
        return self.school_name

class KeySkill(models.Model):
    user = models.ForeignKey(Profile, related_name="skills", null= True, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255, null= True, blank = True)
    
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
       
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', verbose_name=("Comments"), on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.post.title} - {self.name}'
    
    
    
    

    
    
    

      
    
      
    
