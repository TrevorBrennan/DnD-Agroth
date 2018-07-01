from django.shortcuts import render, redirect
from .models import Campaign, PlayerCharacter

# Create your views here.


def set_character(request, pk):
    """
    This will need a much better implementation in the future. I am just doing
    this now to enable development in some other areas
    :param request:
    :param pk:
    :return:
    """

    character = PlayerCharacter.objects.get(pk=pk)
    campaign = Campaign.objects.get(pk=request.session.get('campaign_pk', None))
    if character.player == request.user or campaign.gm in request.user.characters.all():
        request.session['character_name'] = character.name
        request.session['character_pk'] = character.pk
    return redirect('home')


def set_campaign(request, pk):
    """
    This will need a much better implementation in the future. I am just doing
    this now to enable development in some other areas
    :param request:
    :param pk:
    :return:
    """

    campaign = Campaign.objects.get(pk=pk)
    request.session['campaign_pk'] = campaign.pk
    request.session['campaign_name'] = campaign.name
    request.session['character_name'] = None
    request.session['character_pk'] = None
    return redirect('home')
