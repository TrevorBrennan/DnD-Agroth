from django.http import Http404

from authorization.models import Campaign, PlayerCharacter


def exclude_redactions_from_queryset(queryset):
    filtered_qs = queryset
    for item in queryset:
        if item.prime is not None:
            filtered_qs = filtered_qs.exclude(pk=item.pk)
    return filtered_qs


def filter_queryset_for_permitted(queryset, request):
    filtered_qs = queryset
    for item in queryset:
        if not item.permissions.request_has_permissions(request):
            filtered_qs = filtered_qs.exclude(pk=item.pk)
    return filtered_qs


def set_permitted_instance(context, request, object_name):
    instance = context[object_name]

    if instance.prime is not None:
        instance = instance.prime

    if instance.permissions.request_has_permissions(request):
        context[object_name] = instance
        if character_is_gm(context, request=request):
            context['redactions'] = instance.redactions.all()
        return True
    else:
        for redaction in instance.redactions.all():
            if redaction.permissions.request_has_permissions(request):
                context[object_name] = redaction
                return True
        else:
            context[object_name] = None
            raise Http404


def character_is_gm(context, request=None):
    request = request or context['request']
    campaign = Campaign.objects.get(pk=request.session.get('campaign_pk', None))
    character = PlayerCharacter.objects.get(pk=request.session.get('character_pk', None))
    player = character.player
    return campaign.gm == player


def user_is_gm(context):
    request = context['request']
    campaign = Campaign.objects.get(pk=request.session.get('campaign_pk', None))
    return campaign.gm.pk == context['user'].pk
