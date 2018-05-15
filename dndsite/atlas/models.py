import datetime

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils import timezone

from details.models import Tag


class LocationType(models.Model):
    name = models.CharField(max_length=256)
    details = GenericRelation(Tag, related_query_name='location_types')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('atlas:location_type_detail', kwargs={'pk': self.id})


class Location(models.Model):
    name = models.CharField(max_length=256)
    type = models.ForeignKey(LocationType,
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               related_name='children',
                               blank=True,
                               null=True)
    tags = GenericRelation(Tag, related_query_name='locations')

    def __str__(self):
        return "{}, {}".format(self.name, self.type)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('atlas:location_detail', kwargs={'pk': self.id})


