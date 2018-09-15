from django import forms
from .models import Jedi, Planet, Question


class CandidateForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    planet = forms.ModelChoiceField(queryset=Planet.objects.all())

class TestForm(forms.Form):
    pass

# class TestForm(forms.Form):
    # questions = []
    # CHOICES = ((True, 'Yes',), (False, 'No',))
    #
    # for i in range(len(Question.objects.all())):
    #     questions.append(forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES))

# class TestForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         slugs_cnt = kwargs.pop('slugs_cnt', None)
#         super(TestForm, self).__init__(*args, **kwargs)
#
#         CHOICES = ((True, 'Yes',), (False, 'No',))
#         if slugs_cnt:
#             for i in range(1, slugs_cnt + 1):
#                 self.fields['slug_{}'.format(i)] = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


class JediForm(forms.Form):
    jedi = forms.ModelChoiceField(queryset=Jedi.objects.all())
