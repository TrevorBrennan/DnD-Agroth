from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from details.views import DetailHelpers

from .models import Location, LocationType


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


class LocationTypeIndexView(generic.ListView):
    template_name = 'atlas/legend.html'
    context_object_name = 'location_types'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        return LocationType.objects.all()


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
        tags = context['location'].tags.all()
        DetailHelpers.set_detail_collections_from_tags(self.request, context, tags)


class LocationTypeDetailView(generic.DetailView):
    model = LocationType
    template_name = 'atlas/location_type_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.set_location_type(context)
        self.set_details(context)
        return context

    def set_location_type(self, context):
        context['location_type'] = context['locationtype']

    def set_details(self, context):
        tags = context['location_type'].tags.all()
        DetailHelpers.set_detail_collections_from_tags(self.request, context, tags)