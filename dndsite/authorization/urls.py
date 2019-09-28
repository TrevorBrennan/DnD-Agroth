from django.urls import path

from . import views

app_name = 'authorization'
urlpatterns = [
    # ex: /authorization/1
    path('character/<int:pk>', views.set_character, name='set_character'),
    path('campaign/<int:pk>', views.set_campaign, name='set_campaign'),
    path('permissions/add/', views.PermissionsCreateView.as_view(), name='permissions_add'),
    path('permissions/<int:pk>/', views.PermissionsUpdateView.as_view(), name='permission_change'),
]
