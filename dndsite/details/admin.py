from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Chapter, Detail, Relation, RelationMember
from .models import RelationMemberType, RelationType, Source, Tag


# Helper Classes


class EditLinkToInlineObject(object):

    def edit_link(self, instance):
        url = reverse('admin:{0}_{1}_change'.format(
            instance._meta.app_label, instance._meta.model_name),
            args=[instance.pk])

        if instance.pk:
            return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''


# Generic Inline Classes


class GenericTagInline(EditLinkToInlineObject, GenericTabularInline):
    model = Tag
    extra = 1
    readonly_fields = ('edit_link',)


# Inline Classes


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1


class DetailTagInline(admin.TabularInline):
    model = Tag.details.through
    extra = 1


class RelationMemberInline(admin.TabularInline):
    model = RelationMember
    extra = 1


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


# Admin Classes


class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    fields = ['name', 'source', 'permissions']


class DetailAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['detail_text', 'source', 'chapter', 'tags', 'permissions']
    filter_horizontal = ['tags']


class RelationMemberAdmin(admin.ModelAdmin):
    model = RelationMember
    fieldsets = (
        (None, {
            'fields': ('member', 'type')
        }),
        ('Permissions', {
            'fields': ('permissions',)
        }),
    )


class RelationMemberTypeAdmin(admin.ModelAdmin):
    model = RelationMemberType
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('permissions',)
        }),
    )

    inlines = [GenericTagInline]


class RelationAdmin(admin.ModelAdmin):
    model = Relation
    fieldsets = (
        (None, {
            'fields': ('relation_type', 'members')
        }),
        ('Permissions', {
            'fields': ('permissions',)
        }),
    )

    inlines = [GenericTagInline]
    filter_horizontal = ['members']


class RelationTypeAdmin(admin.ModelAdmin):
    model = RelationType
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('permissions',)
        }),
    )

    inlines = [GenericTagInline]


class SourceAdmin(admin.ModelAdmin):
    model = Source
    fields = ['name', 'permissions']

    inlines = [DetailInline]


class TagAdmin(admin.ModelAdmin):
    model = Tag
    fieldsets = (
        (None, {
            'fields': ('pattern',)
        }),
        ('Permissions', {
            'fields': ('permissions',)
        }),
    )

    inlines = [DetailTagInline, RelationMemberInline]


# Admin Class Registration


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(RelationMemberType, RelationMemberTypeAdmin)
admin.site.register(RelationMember, RelationMemberAdmin)
admin.site.register(RelationType, RelationTypeAdmin)
admin.site.register(Relation, RelationAdmin)
