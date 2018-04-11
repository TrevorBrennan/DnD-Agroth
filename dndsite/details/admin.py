from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Detail


class DetailAdmin(admin.ModelAdmin):
    model = Detail
    fields = ['detail_text', 'content_object']


class DetailInline(GenericTabularInline):
    model = Detail
    extra = 3


admin.site.register(Detail, DetailAdmin)
