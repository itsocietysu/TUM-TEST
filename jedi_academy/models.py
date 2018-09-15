# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     jedi = models.BooleanField()
#
#     class Meta:
#         abstract = True
#
#
# class Candidate(UserProfile):
#     planet = models.ForeignKey(Planet, related_name='candidates', null=True, on_delete=models.SET_NULL)
#     age = models.IntegerField()
#     email = models.EmailField(default='', max_length=100)
#
#
# class Jedi(UserProfile):
#     planet = models.ForeignKey(Planet, related_name='jedies', null=True, on_delete=models.SET_NULL)


class Jedi(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, related_name='jedies', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, related_name='candidates', null=True, on_delete=models.SET_NULL)
    age = models.IntegerField()
    email = models.EmailField(default='', max_length=100)
    jedi = models.ForeignKey(Jedi, related_name='padavans', default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Test(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.TextField(max_length=1000)


class TestResult(models.Model):
    test = models.ForeignKey(Test, related_name='test_results', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField()
