from django.shortcuts import render, redirect
from .models import PlayerCharacter

# Create your views here.


def set_character(request, pk):
    """
    This will need a much better implementation in the future. I am just doing
    this now to enable development in some other areas
    :param request:
    :param pk:
    :return:
    """

    character = PlayerCharacter.objects.get(pk=pk)
    if character.player == request.user:
        request.session['character'] = character.name
    return redirect('home')
