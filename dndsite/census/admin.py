from django.contrib import admin

from details.admin import GenericTagInline

from .models import Character

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    model = Character
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('prime', 'permissions')
        }),
    )

    inlines = [GenericTagInline]


admin.site.register(Character, CharacterAdmin)
