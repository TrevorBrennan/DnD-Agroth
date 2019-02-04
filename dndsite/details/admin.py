from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Chapter, Detail, Relation, RelationMember
from .models import RelationMemberType, RelationType, Source, Tag


class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    fields = ['name', 'source', 'permissions']


class DetailAdmin(admin.ModelAdmin):
    model = Tag
    fields = ['detail_text', 'source', 'chapter', 'tags', 'permissions']
    filter_horizontal = ['tags']


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 1


class DetailTagInline(admin.TabularInline):
    model = Tag.details.through
    extra = 1


class SourceAdmin(admin.ModelAdmin):
    model = Source
    fields = ['name', 'permissions']

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


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(RelationMemberType, RelationMemberTypeAdmin)
admin.site.register(RelationMember, RelationMemberAdmin)
admin.site.register(RelationType, RelationTypeAdmin)
admin.site.register(Relation, RelationAdmin)
