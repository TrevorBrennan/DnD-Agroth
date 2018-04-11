from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Detail(models.Model):
    detail_text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        if len(self.detail_text) > 20:
            return "{}...".format(self.detail_text[:17])
        else:
            return self.detail_text
