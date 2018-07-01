from django import template

from atlas.models import Location, LocationType

from authorization.utils import character_is_gm, exclude_redactions_from_queryset, filter_queryset_for_permitted


register = template.Library()


@register.inclusion_tag('atlas/locations_table_widget.html', takes_context=True)
def generate_parents_table(context):
    parents = []
    parent = context['location'].parent
    while parent is not None:
        parents.append(parent)
        parent = parent.parent
    return {
        'locations': reversed(parents)
    }


@register.inclusion_tag('atlas/locations_table_widget.html', takes_context=True)
def generate_children_table(context):

    request = context['request']
    locations = filter_queryset_for_permitted(context['location'].children.all(), request)

    # The GM will have permissions to view a prime and its redactions, so we remove
    # the redactions in that case as they would all point to the same page.
    if character_is_gm(context):
        locations = exclude_redactions_from_queryset(locations)

    return {
        'locations': locations.all().order_by('name'),
    }