from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Campaign, Permissions, PlayerCharacter
from dndsite import settings


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ['name']


class PermissionsForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('admin/css/widgets.css',)
        }
        extra = '' if settings.DEBUG else '.min'
        js = ('/admin/jsi18n', 'jquery%s.js' % extra, 'jquery.init.js', 'core.js', 'SelectBox.js', 'SelectFilter2.js')

    class Meta:
        model = Permissions
        fields = ['name', 'campaigns', 'viewers', 'editors']
        widgets = {
            'campaigns': FilteredSelectMultiple('Campaigns', is_stacked=False),
            'viewers': FilteredSelectMultiple('Characters', is_stacked=False),
            'editors': FilteredSelectMultiple('Characters', is_stacked=False)
        }


class PlayerCharacterForm(forms.ModelForm):

    class Meta:
        model = PlayerCharacter
        fields = ['name']
