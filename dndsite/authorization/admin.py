from django.contrib import admin

from .models import Permissions, PlayerCharacter


class PlayerCharacterAdmin(admin.ModelAdmin):
    model = PlayerCharacter
    fields = ["name", "player", 'is_gm']


class PermissionsAdmin(admin.ModelAdmin):
    model = Permissions
    fields = ['gm_only', 'authorized_characters']
    filter_horizontal = ['authorized_characters']


class PermissionsInline(admin.TabularInline):
    model = Permissions
    fields = ['gm_only', 'authorized_characters']
    filter_horizontal = ['authorized_characters']
    extra = 1


admin.site.register(PlayerCharacter, PlayerCharacterAdmin)
admin.site.register(Permissions, PermissionsAdmin)
