from django.contrib import admin
from .models import *

@admin.register(IndexFront)
class IndexFront(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    
@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ("title_main", "description_main", "image_main")
    
@admin.register(OurService)
class OurService(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    
@admin.register(FeatureDescription)
class FeatureDescription(admin.ModelAdmin):
    list_display = ("title", "description")
    
@admin.register(Feature)
class Feature(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    
@admin.register(LogoCompany)
class LogoCompany(admin.ModelAdmin):
    list_display = ("image", "url")
    
@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ("user", "message")

@admin.register(Designation)
class Designation(admin.ModelAdmin):
    list_display = ("designation",)
    
@admin.register(OurTeam)
class OurTeam(admin.ModelAdmin):
    list_display = ("name", "designation")
    
@admin.register(ContactCompany)
class ContactCompany(admin.ModelAdmin):
    list_display = ("facebook_link", "instagram_link")

    