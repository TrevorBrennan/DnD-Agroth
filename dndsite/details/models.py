from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from authorization.models import Permissions


class Source(models.Model):
    name = models.CharField(max_length=256)
    permissions = models.ForeignKey(Permissions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=256)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='chapters')
    permissions = models.ForeignKey(Permissions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    pattern = models.CharField(max_length=256, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content_object.__str__()


class Detail(models.Model):
    detail_text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='details', blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='details', null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='details', null=True, blank=True)
    permissions = models.ForeignKey(Permissions, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.detail_text) > 20:
            return "{}...".format(self.detail_text[:17])
        else:
            return self.detail_text
