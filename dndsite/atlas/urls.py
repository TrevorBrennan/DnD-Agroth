from django.urls import path

from . import views

app_name = 'atlas'
urlpatterns = [
    # ex: /atlas/
    path('', views.index, name='index'),
    # ex: /atlas/1
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /atlas/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex /atlas/5/vots/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]