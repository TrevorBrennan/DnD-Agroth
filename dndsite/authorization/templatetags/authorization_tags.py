from django import template
from authorization.models import Campaign, PlayerCharacter

register = template.Library()


@register.inclusion_tag('authorization/nav_campaigns_list.html', takes_context=True)
def generate_nav_campaigns_list(context):
    return {
        'campaigns': Campaign.objects.all(),
    }


@register.inclusion_tag('authorization/nav_characters_list.html', takes_context=True)
def generate_nav_characters_list(context):
    request = context['request']
    campaign = Campaign.objects.get(pk=request.session.get('campaign_pk', None))
    characters = PlayerCharacter.objects.filter(player=context['user'], campaigns__id=campaign.pk)
    if campaign.gm in characters:
        characters = PlayerCharacter.objects.filter(campaigns__id=campaign.pk)
    return {
        'characters': characters,
    }
