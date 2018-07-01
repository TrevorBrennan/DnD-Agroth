from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from authorization.utils import filter_queryset_for_permitted, set_permitted_instance
from details.utils import DetailsContextHelper

from .models import Location, LocationType


class IndexView(generic.ListView):
    template_name = 'atlas/location_index.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        locations = filter_queryset_for_permitted(Location.objects.filter(parent=None), self.request)
        return locations


class LocationTypeIndexView(generic.ListView):
    template_name = 'atlas/location_type_index.html'
    context_object_name = 'location_types'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        location_types = filter_queryset_for_permitted(LocationType.objects.all(), self.request)
        return location_types


class LocationDetailView(generic.DetailView):
    model = Location
    template_name = 'atlas/location_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if set_permitted_instance(context, self.request, 'location'):
            self.set_detail_collections(context)
        return context

    def set_detail_collections(self, context):
        DetailsContextHelper.set_detail_collections_from_object(self.request, context, 'location')


class LocationTypeDetailView(generic.DetailView):
    model = LocationType
    template_name = 'atlas/location_type_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if set_permitted_instance(context, self.request, 'locationtype'):
            self.rename_location_type(context)
            self.set_detail_collections(context)
        return context

    def rename_location_type(self, context):
        context['location_type'] = context['locationtype']

    def set_detail_collections(self, context):
        DetailsContextHelper.set_detail_collections_from_object(self.request, context, 'location_type')