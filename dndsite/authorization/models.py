from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PlayerCharacter(models.Model):

    name = models.CharField(max_length=256)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters', null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, ", ".join(self.campaigns.values_list('name', flat=True)))


class Campaign(models.Model):
    name = models.CharField(max_length=256)
    gm = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, related_name='campaigns_as_gm', null=True,
                           blank=True)
    players = models.ManyToManyField(PlayerCharacter, related_name='campaigns')

    def __str__(self):
        return self.name


class Permissions(models.Model):

    name = models.CharField(max_length=256, null=True, blank=True)
    gm_only = models.BooleanField(default=True)
    authorized_characters = models.ManyToManyField(PlayerCharacter, blank=True)
    campaigns = models.ManyToManyField(Campaign, blank=True)

    def __str__(self):
        return self.name or self.permission_description

    @property
    def permission_description(self):
        output = "[{}], [{}]".format(", ".join(self.campaigns.values_list('name', flat=True)), ", ".join(self.authorized_characters.values_list('name', flat=True)))
        if self.gm_only:
            output = "(GM Only) {}".format(output)
        return output

    def request_has_permissions(self, request):

        # Get the relevant values from the session
        character_pk = request.session.get('character_pk', PlayerCharacter())
        campaign_pk = request.session.get('campaign_pk', Campaign())

        # Get the campaign object if the campaign_pk is valid. Otherwise,
        # return false.
        try:
            campaign = Campaign.objects.get(pk=campaign_pk)
        except Campaign.DoesNotExist:
            return False

        if campaign not in self.campaigns.all():
            return False

        # Get the character object if the character name matches a name of a
        # character in the campaign. Otherwise, return false.
        try:
            character = PlayerCharacter.objects.get(pk=character_pk)
        except PlayerCharacter.DoesNotExist:
            return False

        if campaign.gm == character:
            return True
        elif not self.gm_only and character in self.authorized_characters.all():
            return True
        else:
            return False
