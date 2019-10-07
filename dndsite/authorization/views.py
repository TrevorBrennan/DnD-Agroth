from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CampaignForm, PermissionsForm, PlayerCharacterForm
from .models import Campaign, Permissions, PlayerCharacter


# Create your views here.
class CampaignCreateView(LoginRequiredMixin, CreateView):
    model = Campaign
    form_class = CampaignForm
    template_name = 'authorization/pages/campaign_form.html'

    def form_valid(self, form):
        form.instance.gm = self.request.user
        return super().form_valid(form)


class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'authorization/pages/campaign_detail.html'


class PlayerCharacterCreateView(LoginRequiredMixin, CreateView):
    model = PlayerCharacter
    form_class = PlayerCharacterForm
    template_name = 'authorization/pages/player_character_form.html'

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)


class PlayerCharacterDetailView(DetailView):
    model = PlayerCharacter
    template_name = 'authorization/pages/player_character_detail.html'


class PermissionsCreateView(LoginRequiredMixin, CreateView):
    model = Permissions
    form_class = PermissionsForm
    template_name = 'authorization/pages/permissions_form.html'
    success_url = reverse_lazy('home')


class PermissionsUpdateView(LoginRequiredMixin, UpdateView):
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
