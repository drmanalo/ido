from collections import namedtuple
from datetime import datetime

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from guests.invitation import guest_party_by_invite_id_or_404
from guests.models import Guest, MEALS

InviteResponse = namedtuple('InviteResponse', ['guest_pk', 'is_attending', 'meal'])

def invite(request, invite_id):
    party = guest_party_by_invite_id_or_404(invite_id)
    if party.invitation_opened is None:
        # update if this is the first time the invitation was opened
        party.invitation_opened = datetime.now(datetime.UTC)
        party.save()
    if request.method == 'POST':
        for response in _parse_invite_params(request.POST):
            guest = Guest.objects.get(pk=response.guest_pk)
            assert guest.party == party
            guest.is_attending = response.is_attending
            guest.meal = response.meal
            guest.save()
        if request.POST.get('comments'):
            comments = request.POST.get('comments')
            party.comments = comments if not party.comments else '{}; {}'.format(party.comments, comments)
        party.is_attending = party.any_guests_attending
        party.save()
        return HttpResponseRedirect(reverse('confirm', args=[invite_id]))

    return render(request, template_name='guests/invitation.html', context={
        'party': party,
        'meals': MEALS,
        'bride_and_groom' : settings.BRIDE_AND_GROOM,
        'website_url' : settings.WEDDING_WEBSITE_URL,
        'wedding_date' : settings.WEDDING_DATE,
        'wedding_postcode' : settings.WEDDING_POSTCODE,
        'wedding_venue' : settings.WEDDING_VENUE,
    })

def confirm(request, invite_id=None):
    party = guest_party_by_invite_id_or_404(invite_id)
    return render(request, template_name='guests/confirmation.html', context={
        'party': party,
        'support_email' : settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'bride_and_groom' : settings.BRIDE_AND_GROOM,
        'website_url' : settings.WEDDING_WEBSITE_URL,
        'wedding_venue': settings.WEDDING_VENUE,
    })

def _parse_invite_params(params):
    responses = {}
    for param, value in params.items():
        if param.startswith('attending'):
            pk = int(param.split('-')[-1])
            response = responses.get(pk, {})
            response['attending'] = True if value == 'yes' else False
            responses[pk] = response
        elif param.startswith('meal'):
            pk = int(param.split('-')[-1])
            response = responses.get(pk, {})
            response['meal'] = value
            responses[pk] = response

    for pk, response in responses.items():
        yield InviteResponse(pk, response['attending'], response.get('meal', None))