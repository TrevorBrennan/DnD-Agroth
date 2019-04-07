from django.shortcuts import render
from django.views import generic

from authorization.utils import filter_queryset_for_permitted, set_permitted_instance
from details.utils import DetailsContextHelper


from .models import Character


class CharacterIndexView(generic.ListView):
    template_name = 'census/pages/character_index.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        characters = filter_queryset_for_permitted(Character.objects.all(), self.request)
        return characters


class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'census/pages/character_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if set_permitted_instance(context, self.request, 'character'):
            self.set_detail_collections(context)
            self.set_relation_collections(context)
        return context

    def set_detail_collections(self, context):
        DetailsContextHelper.set_detail_collections_from_object(self.request, context, 'character')

    def set_relation_collections(self, context):
        DetailsContextHelper.set_relation_collections_from_object(self.request, context, 'character')
