from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class IndexFront(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    image = models.ImageField()
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class About(models.Model):
    image_main = models.ImageField()
    title_main = models.CharField(max_length=150)
    description_main = models.TextField(max_length=1000)
    
    # Autre description de l'apropos
    image_one = models.ImageField() 
    title_one = models.CharField(max_length=150)
    description_one = models.TextField(max_length=1000)
    image_two = models.ImageField() 
    title_two = models.CharField(max_length=150)
    description_two = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
class OurService(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
  
class FeatureDescription(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Feature(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
class LogoCompany(models.Model):
    image = models.ImageField()
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

class Testimonial(models.Model):
    #user = models.ForeignKey("User", models.CASCADE)
    message = models.TextField(max_length=1000)
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

# Les models qui vons permetre de crée une equipe
class Designation(models.Model):
    designation = models.CharField(max_length=150) 
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True) 

class OurTeam(models.Model):
    name = models.CharField(max_length=150)
    designation = models.ForeignKey(Designation, models.CASCADE)
    photo = models.ImageField() 
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    likedin_link = models.URLField()
    
    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
class ContactCompany(models.Model):
    location = models.CharField(max_length=150)
    number_phone = PhoneNumberField()
    email = models.EmailField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    likedin_link = models.URLField()
    instagram_link = models.URLField()
    youtube_link = models.URLField()

    created = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    