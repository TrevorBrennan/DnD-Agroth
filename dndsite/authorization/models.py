from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from dndsite.utils import get_user_from_request

# Create your models here.


class PlayerCharacter(models.Model):

    name = models.CharField(max_length=256)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters', null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, ", ".join(self.campaigns.values_list('name', flat=True)))

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('authorization:character_detail', kwargs={'pk': self.pk})


class Campaign(models.Model):
    name = models.CharField(max_length=256)
    gm = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns_as_gm', null=True, blank=True)
    players = models.ManyToManyField(PlayerCharacter, related_name='campaigns')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('authorization:campaign_detail', kwargs={'pk': self.pk})


class Permissions(models.Model):

    name = models.CharField(max_length=256, null=True, blank=True)
    campaigns = models.ManyToManyField(Campaign, blank=True)
    viewers = models.ManyToManyField(PlayerCharacter, related_name='view_permissions', blank=True)
    editors = models.ManyToManyField(PlayerCharacter, related_name='edit_permissions', blank=True)

    def __str__(self):
        return self.name or self.permission_description

    @property
    def permission_description(self):
        output = "[{}], [{}]".format(", ".join(self.campaigns.values_list('name', flat=True)), ", ".join(self.viewers.values_list('name', flat=True)))
        return output

    def request_has_view_permissions(self, request):

        # Get the relevant values from the session
        character_pk = request.session.get('character_pk', PlayerCharacter())
        campaign_pk = request.session.get('campaign_pk', Campaign())
        user = get_user_from_request(request)

        # Get the campaign object if the campaign_pk is valid. Otherwise,
        # return false.
        campaign = self.campaigns.filter(pk=campaign_pk).first()
        if not campaign:
            return False

        # If there isn't a character set, False for players and True for GM
        if not character_pk:
            return campaign.gm == user

        # True if the selected character is in the list of viewers
        character = self.viewers.filter(pk=character_pk).first()
        return bool(character)
