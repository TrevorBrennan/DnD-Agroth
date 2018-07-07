from django.contrib import admin

from details.admin import GenericTagInline

from .models import Quest

# Register your models here.


class QuestAdmin(admin.ModelAdmin):
    model = Quest
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('prime', 'permissions')
        }),
    )

    inlines = [GenericTagInline]


admin.site.register(Quest, QuestAdmin)
