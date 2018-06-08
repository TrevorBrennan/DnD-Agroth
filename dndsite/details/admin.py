from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Chapter, Detail, Source, Tag


class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    fields = ['name', 'source']


class DetailAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['detail_text', 'source', 'chapter', 'tags']


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1


class DetailTagInline(admin.TabularInline):
    model = Tag.details.through
    extra = 1


class SourceAdmin(admin.ModelAdmin):
    model = Source
    fields = ['name']

    inlines = [DetailInline]


class TagAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['detail_text', 'source']

    inlines = [DetailTagInline]


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class GenericTagInline(GenericTabularInline):
    model = Tag
    extra = 1


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Tag, TagAdmin)
