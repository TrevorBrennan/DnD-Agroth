from django.contrib import admin

from .models import Location, LocationType
from details.admin import GenericTagInline


class LocationAdmin(admin.ModelAdmin):
    model = Location
    fields = ['name', 'type', 'parent']
    list_display = ('name', 'type')

    inlines = [GenericTagInline]


class LocationTypeAdmin(admin.ModelAdmin):
    model = LocationType
    fields = ['name']

    inlines = [GenericTagInline]


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
