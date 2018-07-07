from django.urls import path

from . import views

app_name = 'endeavours'
urlpatterns = [
    # ex: /endeavours/
    path('', views.QuestIndexView.as_view(), name='quest_index'),
    # ex: /endeavours/1
    path('<int:pk>/', views.QuestDetailView.as_view(), name='quest_detail'),
]