from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from collections import defaultdict

from .models import Source


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'details/index.html'
    context_object_name = 'source_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        return Source.objects.all()


class SourceDetailView(generic.DetailView):
    model = Source
    template_name = 'details/source.html'


class DetailHelpers:

    @staticmethod
    def set_detail_collections(context, tags):
        details = []
        sources = defaultdict(list)
        detail_collections = []
        for tag in tags:
            details.extend(tag.details.all())
        for detail in details:
            sources[detail.source.name].append(detail)
        for source in sorted(sources.keys()):
            detail_collections.append({'name': source,
                                       'label': sources[source][0].pk,
                                       'details': sources[source]})

        context['detail_collections'] = detail_collections
