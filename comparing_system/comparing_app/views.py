from django.shortcuts import render
from .models import Girl
import random
from django.http import HttpResponseRedirect


def add_new(request):
    if request.method == 'GET':
        return render(request, 'comparing_app/add_new.html')
    elif request.method == 'POST':
        girl = Girl(
            name=request.POST['name'],
            description=request.POST['description'],
            photo=request.FILES['picture']
        )
        girl.save()
        return HttpResponseRedirect("/" + str(girl.id))


def index(request):
    if request.method == 'GET':
        girls = Girl.objects.all()
        first_girl = random.choice(girls)
        second_girl = random.choice(girls)
        while first_girl == second_girl:
            second_girl = random.choice(girls)
        return render(request, 'comparing_app/index.html', {'first': first_girl, 'second': second_girl})
    elif request.method == 'POST':
        winner_id = request.POST['win']
        loser_id = request.POST['lose']
        winner = Girl.objects.get(id=winner_id)
        loser = Girl.objects.get(id=loser_id)
        winner.rating += 1
        loser.rating -= 1
        winner.save()
        loser.save()
        return HttpResponseRedirect('/')
# Create your views here.
