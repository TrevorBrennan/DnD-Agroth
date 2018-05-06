from django.urls import path

from . import views

app_name = 'atlas'
urlpatterns = [
    # ex: /atlas/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /atlas/1
    path('<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
]
