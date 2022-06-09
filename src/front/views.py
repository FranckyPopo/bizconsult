import re
from features.models import Newsletter
from .models import *
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

class RequestIndex(View):
    def get(self, request):
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
    
    def post(self, request):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        email = request.POST["email_newlater"]
        
        
        if re.search(regex, email):  
            try:
                data = Newsletter.objects.create(email=email)  
                data.save()
                messages.add_message(request, messages.SUCCESS, 'Félicitation vous venez de vous incrit a la newslatter')
                return HttpResponse("")
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'Cette addresse email existe déjà dans la newslatter')
        
        return self.get(request)

def front_error_404(request):
    return render(request, "front/pages/404.html")


def front_about(request):
    datas = {
        "about": About.objects.first(),
        "features": Feature.objects.all(),
        "teams": OurTeam.objects.all(),
    }
    return render(request, "front/pages/about.html", context=datas)


def front_contact(request):
    return render(request, "front/pages/contact.html")


def front_feature(request):
    return render(request, "front/pages/feature.html", context={"features": Feature.objects.all()})


def front_quote(request):
    return render(request, "front/pages/quote.html", )


def front_service(request):
    datas = {
        "services": OurService.objects.all(),
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, "front/pages/service.html")


def front_team(request):
    return render(request, "front/pages/team.html")


def front_testimonial(request):
    return render(request, "front/pages/testimonial.html")



