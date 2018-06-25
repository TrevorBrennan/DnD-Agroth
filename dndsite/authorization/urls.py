from django.urls import path

from . import views

app_name = 'authorization'
urlpatterns = [
    # ex: /authorization/1
    path('<int:pk>', views.set_character, name='set_character'),
]
