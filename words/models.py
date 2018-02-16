from django.db import models

from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name


class Word(models.Model):
    user = models.ForeignKey(User, related_name='words', on_delete=models.CASCADE)
    word_text = models.CharField(max_length=20)
    context_text = models.CharField(max_length=200)
    translation_text = models.CharField(max_length=100)

    def __str__(self):
        return self.word_text
