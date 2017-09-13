# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import CardGame, Tag
# Register your models here.

admin.site.register(CardGame)

admin.site.register(Tag)