from django.shortcuts import render
from .models import *

def front_error_404(request):
    return render(request, "front/pages/404.html")


def front_about(request):
    return render(request, "front/pages/about.html")


def front_contact(request):
    return render(request, "front/pages/contact.html")


def front_feature(request):
    return render(request, "front/pages/feature.html")


def front_index(request):
    datas = {
        "front_index": IndexFront.objects.first(),
        "about": About.objects.first(),
        "feature_description": FeatureDescription.objects.first(),
        "contact_site": ContactCompany.objects.first(),
        "services": OurService.objects.all(),
        "features": Feature.objects.all(),
        "logos": LogoCompany.objects.all(),
        "testimonials": Testimonial.objects.all(),
        "teams": OurTeam.objects.all(),
        
    }
    return render(request, "front/pages/index.html", context=datas)


def front_quote(request):
    return render(request, "front/pages/quote.html")


def front_service(request):
    return render(request, "front/pages/service.html")


def front_team(request):
    return render(request, "front/pages/team.html")


def front_testimonial(request):
    return render(request, "front/pages/testimonial.html")



