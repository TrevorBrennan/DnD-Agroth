from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Detail, Source


class DetailAdmin(admin.ModelAdmin):
    model = Detail
    fields = ['detail_text', 'source']


class GenericDetailInline(GenericTabularInline):
    model = Detail
    extra = 3


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 3


class SourceAdmin(admin.ModelAdmin):
    model = Source
    fields = ['name']

    inlines = [DetailInline]


admin.site.register(Source, SourceAdmin)
admin.site.register(Detail, DetailAdmin)
