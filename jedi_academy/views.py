# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def main(request):
    return render(request,
                  'main.html', )


def candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            candidate = Candidate(
                name=cd['name'],
                planet=cd['planet'],
                age=cd['age'],
                email=cd['email']
            )
            candidate.save()
            return redirect('/test/{}'.format(candidate.id))
    else:
        form = CandidateForm()
        return render(
            request,
            'candidate.html',
            {'form': form}
        )


def test(request, candidate_id):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
    else:
        form = TestForm()
        return render(
            request,
            'test.html',
            {'form': form}
        )


def jedi(request):
    if request.method == 'POST':
        form = JediForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print('JEDI:                                  ', cd['jedi'])
            jedi_id = 1
            return redirect('/results/{}/'.format(jedi_id))
    else:
        form = JediForm()
        return render(
            request,
            'jedi.html',
            {'form': form}
        )


def results(request, jedi_id):
    tests = []
    jedi = Jedi.objects.get(pk=jedi_id)
    for test in Test.objects.all():
        if (test.candidate.planet.id == jedi.planet.id):
            res = TestResult.objects.filter(test=test)
            tests.append([test.candidate, res])
    print(tests)
    for test in tests:
        print(test[0], test[1])
    return render(
        request,
        'results.html',
        {
         'tests': tests,
         'jedi_id': jedi_id
        }
    )
