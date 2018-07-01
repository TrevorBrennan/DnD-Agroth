from collections import defaultdict
from operator import itemgetter


class DetailsContextHelper:

    @staticmethod
    def set_detail_collections_from_object(request, context, object_name):
        instance = context[object_name]
        if instance.prime is not None:
            tags = instance.prime.tags.all()
        else:
            tags = instance.tags.all()
        DetailsContextHelper.set_detail_collections_from_tags(request, context, tags)

    @staticmethod
    def set_detail_collections_from_tags(request, context, tags):
        details = []
        for tag in tags:
            details.extend(tag.details.all())
        DetailsContextHelper.set_detail_collections(request, context, details)

    @staticmethod
    def set_detail_collections_from_source(request, context, source):
        details = []
        details.extend(source.details.all())
        DetailsContextHelper.set_detail_collections(request, context, details)
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
