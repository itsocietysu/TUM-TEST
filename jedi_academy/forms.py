from django import forms
from django.forms import formset_factory
from .models import Jedi, Planet, Question


class CandidateForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    planet = forms.ModelChoiceField(queryset=Planet.objects.all())


class TestForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=((True, 'True'), (False, 'False')))


class JediForm(forms.Form):
    jedi = forms.ModelChoiceField(queryset=Jedi.objects.all())
