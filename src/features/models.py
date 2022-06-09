from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField()
    profession = models.CharField(max_length=150)

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
class Quote(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    service = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    
    