from collections import defaultdict
from operator import itemgetter


class DetailsContextHelper:

    @staticmethod
    def get_tags_from_object(context, object_name):
        instance = context[object_name]
        if instance.prime is not None:
            tags = instance.prime.tags.all()
        else:
            tags = instance.tags.all()
        return tags

    @staticmethod
    def set_detail_collections_from_object(request, context, object_name):
        tags = DetailsContextHelper.get_tags_from_object(context, object_name)
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

    @staticmethod
    def set_relation_collections_from_object(request, context, object_name):
        tags = DetailsContextHelper.get_tags_from_object(context, object_name)
        DetailsContextHelper.set_relation_collections_from_tags(request, context, tags)


    @staticmethod
    def set_relation_collections_from_tags(request, context, tags):
        relation_members = []
        for tag in tags:
            relation_members.extend(tag.relation_members.all())
        DetailsContextHelper.set_relation_collections(request, context, relation_members)


    @staticmethod
    def set_relation_collections(request, context, relation_members):
        cards = defaultdict(list)
        relation_collections = []
        for relation_member in relation_members:
            if relation_member.permissions.request_has_permissions(request):
                for relation in relation_member.relations.all():
                    if relation.permissions.request_has_permissions(request):
                        # Get the other relation member here so it is available in context
                        relation_info = {'other': relation.other_member(relation_member),
                                         'relation': relation}
                        cards[relation_member].append(relation_info)
        for key, value in cards.items():

            relation_collections.append({'label': key.pk,
                                         'relation_type': key.type.name,
                                         'relation_infos': value})
        relation_collections = sorted(relation_collections, key=itemgetter('relation_type'))
        context['relation_collections'] = relation_collections



