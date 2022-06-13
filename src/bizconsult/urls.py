from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from front import views
from features.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RequestIndex.as_view(), name="front_index"),
    path('about/', views.front_about, name="front_about"),
    path('contact/', RequestContact.as_view(), name="front_contact"),
    path('feature/', views.front_feature, name="front_feature"),
    path('quote/', PageQuote.as_view(), name="front_quote"),
    path('service/', views.front_service, name="front_service"),
    path('team/', views.front_team, name="front_team"),
    path('testimonial/', views.front_testimonial, name="front_testimonial"),
    path('404/', views.front_error_404, name="front_error_404"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )