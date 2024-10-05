from django.db import models
from .models import profile

class Room(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(profile, on_delete=models.SET_NULL, null= True, blank=True)
    featured_image = models.ImageField(upload_to='static/images', null=True, blank=True, default='default.jpg')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    section = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.section

    
    
    
    

# Create your models here.
