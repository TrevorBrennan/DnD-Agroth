from django.urls import path

from . import views

app_name = 'atlas'
urlpatterns = [
    # ex: /atlas/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /atlas/1
    path('<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    # ex: /atlas/legend/
    path('legend/', views.LocationTypeIndexView.as_view(), name='location_type_index'),
    # ex: /atlas/legend/1
    path('legend/<int:pk>/', views.LocationTypeDetailView.as_view(), name='location_type_detail'),
]
