from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from collections import defaultdict
from operator import itemgetter

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.set_detail_collections(context)
        return context

    def set_detail_collections(self, context):
        DetailHelpers.set_detail_collections_from_source(self.request, context, context['source'])


class DetailHelpers:

    @staticmethod
    def set_detail_collections_from_tags(request, context, tags):
        details = []
        for tag in tags:
            details.extend(tag.details.all())
        DetailHelpers.set_detail_collections(request, context, details)

    @staticmethod
    def set_detail_collections_from_source(request, context, source):
        details = []
        details.extend(source.details.all())
        DetailHelpers.set_detail_collections(request, context, details)
        for collection in context['detail_collections']:
            if collection['chapter'] is not None:
                collection['name'] = collection['chapter'].name
            else:
                collection['name'] = collection['chapter']

    @staticmethod
    def set_detail_collections(request, context, details):
        cards = defaultdict(list)
        detail_collections = []
        for detail in details:
            if detail.source is None or detail.source.permissions.request_has_permissions(request):
                if detail.chapter is None or detail.chapter.permissions.request_has_permissions(request):
                    if detail.permissions.request_has_permissions(request):
                        cards[(detail.source, detail.chapter)].append(detail)
        for key, value in cards.items():
            source, chapter = key
            if chapter is None:
                label = "{}".format(source.pk)
                name = "{}".format(source)
            else:
                label = "{}_{}".format(source.pk, chapter.pk)
                name = "{} - {}".format(source, chapter)
            detail_collections.append({'source': source,
                                       'chapter': chapter,
                                       'name': name,
                                       'label': label,
                                       'details': value})
        detail_collections = sorted(detail_collections, key=itemgetter('name'))
        context['detail_collections'] = detail_collections
