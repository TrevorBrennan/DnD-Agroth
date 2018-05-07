from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Detail, Source, Tag


class DetailTagInline(admin.TabularInline):
    model = Tag.details.through
    extra = 1


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1


class TagAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['detail_text', 'source']

    inlines = [DetailTagInline]


class DetailAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['detail_text', 'source', 'tags']


class GenericTagInline(GenericTabularInline):
    model = Tag
    extra = 1


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class SourceAdmin(admin.ModelAdmin):
    model = Source
    fields = ['name']

    inlines = [DetailInline]


admin.site.register(Detail, DetailAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Tag, TagAdmin)
