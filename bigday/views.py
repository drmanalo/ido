from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={
        'couple_name': settings.BRIDE_AND_GROOM,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'website_url': settings.WEDDING_WEBSITE_URL,
        'wedding_location': settings.WEDDING_VENUE,
        'wedding_date': settings.WEDDING_DATE,
    })