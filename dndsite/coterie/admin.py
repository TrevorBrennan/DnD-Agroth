from django.contrib import admin

from details.admin import GenericTagInline

from .models import Faction

# Register your models here.


class FactionAdmin(admin.ModelAdmin):
    model = Faction
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('prime', 'permissions')
        }),
    )

    inlines = [GenericTagInline]


admin.site.register(Faction, FactionAdmin)
