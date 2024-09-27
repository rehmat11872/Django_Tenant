from django.template import Library
from core.models import SiteSetting

register = Library() 

@register.inclusion_tag('includes/header.html') 
def header_view(request):
    branding = SiteSetting.objects.first()
    if branding:
        color = branding.color
        logo = branding.logo


    else:
        color = None
        logo = None
    

    print(color, 'color')
    context = {
        'request' : request,
        'color' : color,
        'logo':logo,
    }
    return context