from django.http import Http404

from .models import Campaign, PlayerCharacter
from dndsite.utils import get_user_from_request

def exclude_redactions_from_queryset(queryset):
    filtered_qs = queryset
    for item in queryset:
        if item.prime is not None:
            filtered_qs = filtered_qs.exclude(pk=item.pk)
    return filtered_qs


def filter_queryset_for_permitted(queryset, request):
    filtered_qs = queryset
    for item in queryset:
        if not item.permissions.request_has_view_permissions(request):
            filtered_qs = filtered_qs.exclude(pk=item.pk)
    return filtered_qs


def set_permitted_instance(context, request, object_name):
    instance = context[object_name]

    if instance.prime is not None:
        instance = instance.prime

    if instance.permissions.request_has_view_permissions(request):
        context[object_name] = instance
        if user_as_gm(context, request=request):
            context['redactions'] = instance.redactions.all()
        return True
    else:
        for redaction in instance.redactions.all():
            if redaction.permissions.request_has_view_permissions(request):
                context[object_name] = redaction
                return True
        else:
            context[object_name] = None
            raise Http404


def user_as_gm(context, request=None):
    """
    Identifies if the currently logged is user is acting as the GM of the
    currently selected campaign. If the user is the GM, but has selected a
    character, they are not acting as the GM.
    """
    request = request or context['request']
    character_pk = request.session.get('character_pk', None)
    if character_pk:
        return False
    else:
        return user_is_gm(context, request)


def user_is_gm(context, request=None):
    """
    Identifies if the currently logged in user is the GM of the currently
    selected campaign.
    """
    request = request or context['request']
    campaign = Campaign.objects.get(pk=request.session.get('campaign_pk', None))
    return campaign.gm == get_user_from_request(request)
