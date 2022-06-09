from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.front_index, name="front_index"),
    path('about/', views.front_about, name="front_about"),
    path('contact/', views.front_contact, name="front_contact"),
    path('feature/', views.front_feature, name="front_feature"),
    path('quote/', views.front_quote, name="front_quote"),
    path('service/', views.front_service, name="front_service"),
    path('team/', views.front_team, name="front_team"),
    path('testimonial/', views.front_testimonial, name="front_testimonial"),
    path('404/', views.front_testimonial, name="front_error_404"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )