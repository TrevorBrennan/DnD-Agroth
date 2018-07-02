from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse


from details.models import Tag
from authorization.models import Permissions


class Character(models.Model):
    name = models.CharField(max_length=256)

    prime = models.ForeignKey('self', on_delete=models.CASCADE, related_name='redactions', null=True, blank=True)
    permissions = models.ForeignKey(Permissions, on_delete=models.CASCADE)
    tags = GenericRelation(Tag, related_query_name='characters')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('census:character_detail', kwargs={'pk': self.pk})

    def is_prime(self):
        """
        Determines if this object is the prime object or a redacted copy.
        :return: True if Prime. False if Redacted Copy.
        """
        if self.prime is None:
            return True
        else:
            return False
