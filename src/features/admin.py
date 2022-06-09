from django.contrib import admin
from .models import *

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ("username",)
    
@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    list_display = ("email", "created")

@admin.register(Quote)
class Quote(admin.ModelAdmin):
    list_display = ("name", "email", "service")

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ("name", "email", "subject")
