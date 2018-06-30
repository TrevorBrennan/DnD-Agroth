from django.contrib import admin

from .models import Location, LocationType
from details.admin import GenericTagInline


class LocationAdmin(admin.ModelAdmin):
    model = Location
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'parent')
        }),
        ('Permissions', {
            'fields': ('prime', 'permissions')
        }),
    )

    list_display = ('name', 'type')

    inlines = [GenericTagInline]


class LocationTypeAdmin(admin.ModelAdmin):
    model = LocationType
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('prime', 'permissions')
        }),
    )

    inlines = [GenericTagInline]


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
