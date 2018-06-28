from django.urls import path

from . import views

app_name = 'authorization'
urlpatterns = [
    # ex: /authorization/1
    path('character/<int:pk>', views.set_character, name='set_character'),
    path('campaign<int:pk>', views.set_campaign, name='set_campaign'),
]
