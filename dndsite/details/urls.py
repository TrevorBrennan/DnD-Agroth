from django.urls import path

from . import views

app_name = 'details'
urlpatterns = [
    # ex: /details/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /details/1
    path('<int:pk>/', views.SourceDetailView.as_view(), name='source_detail'),
]
