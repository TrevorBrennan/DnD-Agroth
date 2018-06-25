from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PlayerCharacter(models.Model):

    name = models.CharField(max_length=256)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters', null=True, blank=True)
    is_gm = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Permissions(models.Model):

    gm_only = models.BooleanField(default=True)
    authorized_characters = models.ManyToManyField(PlayerCharacter)

    def __str__(self):
        output = ""
        if self.gm_only:
            output = "GM Only"
        for character in self.authorized_characters.all():
            output = "{}, {}".format(output, character.name)
        return output

    def request_has_permissions(self, request):
        name = request.session.get('character', 'Guest')
        try:
            character = PlayerCharacter.objects.get(name=name)
        except PlayerCharacter.DoesNotExist:
            return False
        if character.is_gm:
            return True
        elif not self.gm_only and character in self.authorized_characters.all():
            return True
        else:
            return False
