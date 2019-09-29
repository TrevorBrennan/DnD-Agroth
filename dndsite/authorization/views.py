from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import PermissionsForm
from .models import Campaign, Permissions, PlayerCharacter


# Create your views here.

class CharacterDetailView(DetailView):
    model = PlayerCharacter
    template_name = 'authorization/pages/player_character_detail.html'


class PermissionsCreateView(CreateView):
    model = Permissions
    form_class = PermissionsForm
    template_name = 'authorization/pages/permissions_form.html'
    success_url = reverse_lazy('home')


class PermissionsUpdateView(UpdateView):
    model = Permissions
    form_class = PermissionsForm
    template_name = 'authorization/pages/permissions_form.html'
    success_url = reverse_lazy('home')


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
