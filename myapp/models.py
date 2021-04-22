from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length = 255)
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 255, default = 'uncategorized')
    content = RichTextField(blank = True, null = True)
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    
    def total_likes(self):
        return self.likes.count()
    
      
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    
    def get_absolute_url(self):
        return reverse("detailed_view", kwargs={"pk": self.pk}) 
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
       
    def get_absolute_url(self):
        return reverse("detailed_view", kwargs={"pk": self.pk}) 
    
    class Meta:
        verbose_name_plural = "Categories"
        

class Profile(models.Model):
    user  = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True,  upload_to = "images/profile/")
    website  = models.CharField(max_length = 255, null= True, blank = True)
    facebook = models.CharField(max_length = 255, null= True, blank = True)
    linkedin = models.CharField(max_length = 255, null= True, blank = True)
    instagram = models.CharField(max_length = 255, null= True, blank = True)
    twitter = models.CharField(max_length = 255, null= True, blank = True)
    
    
    def __str__(self):
        return str(self.user)
    
    
    

      
    
      
    
