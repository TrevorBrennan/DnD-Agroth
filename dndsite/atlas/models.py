import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Detail(models.Model):
    detail_text = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        if len(self.detail_text) > 20:
            return "{}...".format(self.detail_text[:17])
        else:
            return self.detail_text


class LocationType(models.Model):
    name = models.CharField(max_length=256)
    details = models.ManyToManyField(Detail,
                                     blank=True)

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
    details = models.ManyToManyField(Detail,
                                     blank=True)

    def __str__(self):
        return self.name



