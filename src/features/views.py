import re
import json
from front.models import *
from .models import *
from django.shortcuts import render
from django.views import View
from django.db.utils import IntegrityError
from django.http import HttpResponse

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
                                "message": "Cette addresse email est déjà inscrite dans la newslatter.",
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
                                "message": "Veuillez remplir le champ pour vous incrit a la newslater.",
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
                                "message": "Veuillez entrer une addresse email valide.",
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
        
        if (
            re.search(regex, email) 
            and 0 < len(name) <= 150 
            and 0 < len(subject) <= 150
            and 0 < len(message) <= 1000
            and not name.isspace()
            and not subject.isspace()
            and not message.isspace()
        ):
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
                        "message": "Vôtre demande a échoué, veuillez vérifier les différents champs et résayer",
                        "icon": "error",
                        "title": "Contact"
                    }
                })
            }
        )
     
class PageQuote(View):
    def get(self, request):
        return render(request, "front/pages/quote.html")
    
    def post(self, request):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        name = request.POST["name"]
        email = request.POST["email"]
        service = request.POST["Services"]
        message = request.POST["message"]

        if(
            re.search(regex, email) 
            and 0 < len(name) <= 150
            and 0 < len(service) <= 150
            and 0 < len(message) <= 1000
            and not name.isspace()
            and not service.isspace()
            and not message.isspace()
        ):
            Quote.objects.create(email=email, name=name, message=message, service=service)
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps({
                        "showMessage": {
                            "message": "Vôtre demande de devis a bien été envoyé.",
                            "icon": "success",
                            "title": "Devis"
                        }
                    })
                }
            )
        return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps({
                        "showMessage": {
                            "message": "Imposible d'envoyer la demande de devis, veuillez vérifier les différents champs et résayer.",
                            "icon": "error",
                            "title": "Devis"
                        }
                    })
                }
            )

