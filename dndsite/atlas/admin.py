from django.contrib import admin

from .models import Location, LocationType
from details.admin import DetailInline


class LocationAdmin(admin.ModelAdmin):
    model = Location
    fields = ['name', 'type', 'parent']
    list_display = ('name', 'type')

    inlines = [DetailInline]


class LocationTypeAdmin(admin.ModelAdmin):
    model = LocationType
    fields = ['name']

    inlines = [DetailInline]


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
