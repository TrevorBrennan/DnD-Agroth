from django.urls import path

from . import views

app_name = 'atlas'
urlpatterns = [
    # ex: /atlas/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /atlas/1
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /atlas/1/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex /atlas/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]