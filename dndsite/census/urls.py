from django.urls import path

from . import views

app_name = 'census'
urlpatterns = [
    # ex: /census/
    path('', views.CharacterIndexView.as_view(), name='character_index'),
    # ex: /character/1
    path('<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
]