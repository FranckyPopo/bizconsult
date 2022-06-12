from re import search
import json
from features.models import *
from .models import *
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
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

        if search(regex, email):  
            try:
                data = Newsletter.objects.create(email=email)  
                data.save()
                return HttpResponse(
                    status=204,
                    headers={
                        "HX-Trigger": json.dumps({
                            "showMessage": {
                                "message": "Félicitation vous venez de vous inscrit a la newslater",
                                "icon": "success",
                                "title": "Newslater"
                            }
                        })
                    }
                )
            except IntegrityError:
                return HttpResponse(
                    status=204, 
                    headers={
                        "HX-Trigger": json.dumps({
                            "showMessage": {
                                "message": "Cette addresse email est déjà inscrite dans la newslatter",
                                "icon": "info",
                                "title": "Newslater"
                            }
                        })
                    }
                )
        elif not email:
            return HttpResponse(
                    status=204, 
                    headers={
                        "HX-Trigger": json.dumps({
                            "showMessage": {
                                "message": "Veuillez remplir le champ pour vous incrit a la newslater",
                                "icon": "error",
                                "title": "Newslater"
                            }
                        })
                    }
                )
        return HttpResponse(
                    status=204, 
                    headers={
                        "HX-Trigger": json.dumps({
                            "showMessage": {
                                "message": "Veuillez entrer une addresse email valid",
                                "icon": "error",
                                "title": "Newslater"
                            }
                        })
                    }
                )
     
class RequestContact(View):
    def get(self, request):
        return render(request, "front/pages/contact.html")
    
    def post(self, request):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"        
        name = request.POST["name"]     
        email = request.POST["email"]     
        subject = request.POST["subject"]    
        message = request.POST["message"]   
        
        print(bool(name), bool(email), bool(subject), bool(message))
        
        if search(regex, email) and len(name) <= 150 and len(subject) <= 150 and len(message) <= 1000:
            Contact.objects.create(email=email, name=name, message=message, subject=subject)
            return HttpResponse(
                    status=204,
                    headers={
                        "HX-Trigger": json.dumps({
                            "showMessage": {
                                "message": "Vôtre demande a été bien pris en charge",
                                "icon": "success",
                                "title": "Contact"
                            }
                        })
                    }
                )
        return HttpResponse(
            status=204,
            headers={
                "HX-Trigger": json.dumps({
                    "showMessage": {
                        "message": "Vôtre demande a échoué, veuillez vérifier vôtre les différent champs et résayer",
                        "icon": "error",
                        "title": "Contact"
                    }
                })
            }
        )
        
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



