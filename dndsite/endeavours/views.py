from django.shortcuts import render
from django.views import generic

from authorization.utils import filter_queryset_for_permitted, set_permitted_instance
from details.utils import DetailsContextHelper


from .models import Quest


class QuestIndexView(generic.ListView):
    template_name = 'endeavours/pages/quest_index.html'
    context_object_name = 'quest_list'

    def get_queryset(self):
        """
        Return a list of locations without parents
        """
        quests = filter_queryset_for_permitted(Quest.objects.all(), self.request)
        return quests


class QuestDetailView(generic.DetailView):
    model = Quest
    template_name = 'endeavours/pages/quest_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if set_permitted_instance(context, self.request, 'quest'):
            self.set_detail_collections(context)
        return context

    def set_detail_collections(self, context):
        DetailsContextHelper.set_detail_collections_from_object(self.request, context, 'quest')
