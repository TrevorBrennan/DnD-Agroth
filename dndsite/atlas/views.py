from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Location


class IndexView(generic.ListView):
    template_name = 'atlas/index.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        return Location.objects.filter(
            parent=None
        )


class LocationDetailView(generic.DetailView):
    model = Location
    template_name = 'atlas/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.set_parents(context)
        self.set_details(context)
        return context

    def set_parents(self, context):
        parents = []
        parent = context['location'].parent
        while parent is not None:
            parents.append(parent)
            parent = parent.parent
        if len(parents) > 0:
            context['parents'] = parents

    def set_details(self, context):
        details = []
        tags = context['location'].tags.all()
        for tag in tags:
            details.extend(tag.details.all())
        context['details'] = details
