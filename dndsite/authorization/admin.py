from django.contrib import admin

from .models import Campaign, Permissions, PlayerCharacter


class PlayershipInline(admin.TabularInline):
    model = Campaign.players.through


class CampaignAdmin(admin.ModelAdmin):
    model = Campaign
    fields = ['name', 'gm']
    inlines = [PlayershipInline]
    exclude = ['players']


class PermissionsAdmin(admin.ModelAdmin):
    model = Permissions
    fields = ['name', 'campaigns', 'viewers', 'editors']
    filter_horizontal = ['campaigns', 'viewers', 'editors']

    list_display = ['name', 'permission_description']


class PermissionsInline(admin.TabularInline):
    model = Permissions
    fields = ['name', 'campaigns', 'viewers', 'editors']
    filter_horizontal = ['campaigns', 'viewers', 'editors']
    extra = 1


class PlayerCharacterAdmin(admin.ModelAdmin):
    model = PlayerCharacter
    fields = ['name', 'player']
    inlines = [PlayershipInline]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Permissions, PermissionsAdmin)
admin.site.register(PlayerCharacter, PlayerCharacterAdmin)
