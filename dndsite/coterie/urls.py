from django.urls import path

from . import views

app_name = 'coterie'
urlpatterns = [
    # ex: /coterie/
    path('', views.FactionIndexView.as_view(), name='faction_index'),
    # ex: /coterie/1
    path('<int:pk>/', views.FactionDetailView.as_view(), name='faction_detail'),
]