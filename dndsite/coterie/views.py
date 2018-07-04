from django.shortcuts import render
from django.views import generic

from authorization.utils import filter_queryset_for_permitted, set_permitted_instance
from details.utils import DetailsContextHelper


from .models import Faction


class FactionIndexView(generic.ListView):
    template_name = 'coterie/pages/faction_index.html'
    context_object_name = 'faction_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        characters = filter_queryset_for_permitted(Faction.objects.all(), self.request)
        return characters


class FactionDetailView(generic.DetailView):
    model = Faction
    template_name = 'coterie/pages/faction_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if set_permitted_instance(context, self.request, 'faction'):
            self.set_detail_collections(context)
        return context

    def set_detail_collections(self, context):
        DetailsContextHelper.set_detail_collections_from_object(self.request, context, 'faction')
