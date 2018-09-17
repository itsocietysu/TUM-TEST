# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.core.mail import send_mail
from django.http import HttpResponse
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
    TestFormSet = formset_factory(TestForm, extra=Question.objects.count())
    if request.method == "POST":
        formset = TestFormSet(request.POST)
        if formset.is_valid():
            new_test = Test(candidate_id=candidate_id)
            new_test.save()
            for form, q in zip(formset, Question.objects.all()):
                if form.is_valid():
                    new_result = TestResult(answer=form.cleaned_data['answer'], question_id=q.id, test_id=new_test.id)
                    new_result.save()
        return redirect('/')
    else:
        formset = TestFormSet()
        for form, q in zip(formset, Question.objects.all()):
            form['answer'].label = q.text
        context = {
            'formset': formset,
        }
        return render(request, 'test.html', context)



def jedi(request):
    if request.method == 'POST':
        form = JediForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            jedi_id = cd['jedi'].id
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
        if (test.candidate.planet.id == jedi.planet.id and not test.candidate.jedi):
            res = TestResult.objects.filter(test=test)
            tests.append([test.candidate, res])
    return render(
        request,
        'results.html',
        {
         'tests': tests,
         'jedi_id': jedi_id
        }
    )

def padawan_count(jedi_id):
    return len(Candidate.objects.filter(jedi_id=jedi_id))


def accept(request, jedi_id, candidate_id):
    padavan = Candidate.objects.get(pk=candidate_id)
    jedi = Jedi.objects.get(pk=jedi_id)
    if padawan_count(jedi_id) <= 3:
        padavan.jedi = jedi
        padavan.save()
        email_subject = 'Вы приняты!'
        email_body = 'Джедай {} принял вас в подаваны!'.format(jedi.name)
        send_mail(email_subject, email_body, 'YOUR EMAIL HERE', [padavan.email], fail_silently=False)

                                # INSERT YOUR EMAIL

        return redirect('/results/{}/'.format(jedi_id))
    else:
        return HttpResponse("У вас уже много падаванов")


def all_padawans(request):
    padawans = []
    for jedi in Jedi.objects.all():
        padawans.append([jedi, str(padawan_count(jedi.id))])
    return render(request, 'all_padawans.html', {'padawans': padawans})


def more_one_padawan(request):
    padawans = []
    for jedi in Jedi.objects.all():
        padawans_count = padawan_count(jedi.id)
        if padawans_count > 1:
            padawans.append([jedi, str(padawans_count)])
    return render(request, 'more_one_padawan.html', {'padawans': padawans})
