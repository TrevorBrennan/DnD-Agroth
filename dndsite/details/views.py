from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'details/index.html'
    context_object_name = 'location_list'