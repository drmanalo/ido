from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={
        'bride_and_groom': settings.BRIDE_AND_GROOM,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'wedding_date': settings.WEDDING_DATE,
        'wedding_postcode': settings.WEDDING_POSTCODE,
        'wedding_venue': settings.WEDDING_VENUE,
        'website_url': settings.WEDDING_WEBSITE_URL,
    })