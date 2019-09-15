"""dndsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from dndsite.views import SignUpView

urlpatterns = [
    path('', TemplateView.as_view(template_name='dndsite/pages/home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('polls/', include('polls.urls')),
    path('details/', include('details.urls')),
    path('atlas/', include('atlas.urls')),
    path('census/', include('census.urls')),
    path('coterie/', include('coterie.urls')),
    path('endeavours/', include('endeavours.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('authorization/', include('authorization.urls')),
]
