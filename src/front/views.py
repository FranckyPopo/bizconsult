from features.models import *
from .models import *
from django.shortcuts import render
           
def front_error_404(request):
    return render(request, "front/pages/404.html")


def front_about(request):
    datas = {
        "about": About.objects.first(),
        "features": Feature.objects.all(),
        "teams": OurTeam.objects.all(),
    }
    return render(request, "front/pages/about.html", context=datas)


def front_feature(request):
    return render(request, "front/pages/feature.html", context={"features": Feature.objects.all()})


def front_service(request):
    datas = {
        "services": OurService.objects.all(),
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, "front/pages/service.html", context=datas)


def front_team(request):
    return render(request, "front/pages/team.html")


def front_testimonial(request):
    return render(request, "front/pages/testimonial.html")



