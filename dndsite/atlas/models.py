import datetime

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone

from details.models import Detail


class LocationType(models.Model):
    name = models.CharField(max_length=256)
    details = GenericRelation(Detail, related_query_name='location_types')

    def __str__(self):
        return self.name


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
    details = GenericRelation(Detail, related_query_name='locations')

    def __str__(self):
        return "{}, {}".format(self.name, self.type)



