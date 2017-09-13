# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name



class CardGame(models.Model):
    name = models.CharField(max_length=50)
    max_number_of_players = models.IntegerField()
    min_number_of_players = models.IntegerField()
    difficulty = models.IntegerField();
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name

    def get_difficulty(self):
        if self.difficulty == 1:
            return "Easy"
        elif self.difficulty == 2:
            return "Medium"
        else:
            return "Hard"





