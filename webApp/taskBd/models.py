from statistics import mode
from django.db import models


class taskiq(models.Model):
    # name = models.CharField('name', max_length=20)
    question = models.CharField('question', max_length=100)
    corAnsver = models.CharField('corAnsver', max_length=5)
    answer1 = models.CharField('answer1', max_length=100)
    answer2 = models.CharField('answer2', max_length=100)
    answer3 = models.CharField('answer3', max_length=100)
    answer4 = models.CharField('answer4', max_length=100)
    answer5 = models.CharField('answer5', max_length=100)
    answer6 = models.CharField('answer6', max_length=100)

    def __str__(self):
        return self.question
