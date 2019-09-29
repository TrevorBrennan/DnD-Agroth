from django.urls import path

from . import views

app_name = 'authorization'
urlpatterns = [
    # ex: /authorization/1
    path('character/set_active/<int:pk>', views.set_character, name='set_character'),
    path('character/<int:pk>', views.CharacterDetailView.as_view(), name='character_detail'),
    path('campaign/set_active/<int:pk>', views.set_campaign, name='set_campaign'),
    path('permissions/add/', views.PermissionsCreateView.as_view(), name='permissions_add'),
    path('permissions/<int:pk>/', views.PermissionsUpdateView.as_view(), name='permission_change'),
]
