# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from .models import CardGame
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

def index(request):
    return render(request,'GamePlay/index.html')

class CatalogView(generic.ListView):
    template_name = 'GamePlay/catalog.html'
    context_object_name = 'card_game_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return CardGame.objects
