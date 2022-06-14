from front.models import ContactCompany

def info_site(request):
    return {"contact_site": ContactCompany.objects.first()}