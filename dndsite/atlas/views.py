from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from collections import defaultdict

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
        sources = defaultdict(list)
        detail_collections = []
        tags = context['location'].tags.all()
        for tag in tags:
            details.extend(tag.details.all())
        for detail in details:
            sources[detail.source.name].append(detail)
        for source in sorted(sources.keys()):
            detail_collections.append({'name': source,
                                       'label': sources[source][0].pk,
                                       'details': sources[source]})

        context['detail_collections'] = detail_collections
