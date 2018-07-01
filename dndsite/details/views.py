from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Source
from .utils import DetailsContextHelper


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'details/pages/source_index.html'
    context_object_name = 'source_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        all_sources = Source.objects.all()
        sources = all_sources
        for source in all_sources:
            if not source.permissions.request_has_permissions(self.request):
                sources = sources.exclude(pk=source.pk)
        return sources


class SourceDetailView(generic.DetailView):
    model = Source
    template_name = 'details/pages/source_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.set_detail_collections(context)
        return context

    def set_detail_collections(self, context):
        DetailsContextHelper.set_detail_collections_from_source(self.request, context, context['source'])
