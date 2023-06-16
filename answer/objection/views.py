from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Objections


def objections(request):

    random_objection = Objections.objects.order_by('?')[:1]
    return render(request, 'objection/objections.html', {
        'random_objection': random_objection
    })

def objectionsAll(request):

    objection = Objections.objects.all()
    return render(request, 'objection/objections_all.html', {
        'random_objection': objection
    })