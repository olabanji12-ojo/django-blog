from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(default='default.jpg', null=True, blank=True, upload_to='static/images')
    email = models.EmailField(null=True, blank=True)
      
    def __str__(self):
        return str(self.name)
        
        
        
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
     
    
    def __str__(self):
        return str(self.bio)
        
    
    

    
    
    
    

    
    

# Create your models here.
