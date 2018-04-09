from django.contrib import admin

from .models import Detail, Location, LocationType
# Register your models here.


class LocationDetailInline(admin.TabularInline):
    model = Location.details.through
    extra = 3


class LocationTypeDetailInline(admin.TabularInline):
    model = LocationType.details.through
    extra = 3


class LocationAdmin(admin.ModelAdmin):
    model = Location
    fields = ['name', 'type']
    filter_horizontal = ('details',)
    inlines = [LocationDetailInline]


class LocationTypeAdmin(admin.ModelAdmin):
    model = LocationType
    fields = ['name']
    filter_horizontal = ('details',)
    inlines = [LocationTypeDetailInline]


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
