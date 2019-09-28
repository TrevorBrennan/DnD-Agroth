from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Permissions
from dndsite import settings


class PermissionsForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('admin/css/widgets.css',)
        }
        extra = '' if settings.DEBUG else '.min'
        js = ('/admin/jsi18n', 'jquery%s.js' % extra, 'jquery.init.js', 'core.js', 'SelectBox.js', 'SelectFilter2.js')

    class Meta:
        model = Permissions
        fields = ['name', 'gm_only', 'authorized_characters', 'campaigns']
        widgets = {
            'authorized_characters': FilteredSelectMultiple('Characters', is_stacked=False),
            'campaigns': FilteredSelectMultiple('Campaigns', is_stacked=False)
        }
