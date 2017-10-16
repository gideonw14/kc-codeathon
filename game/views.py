from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task, Player
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.contrib.auth.decorators import login_required


def getTaskList():
	all_tasks = list()
	with open("game/tasks.json","r") as json_file:
		json_dict = json.loads(json_file.read())
	for task_data in json_dict["tasks"]:
		all_tasks.append(Task(task_data))
	return all_tasks

@login_required()
@csrf_exempt
def game(request):
    # import ipdb; ipdb.set_trace()
    # import ipdb; ipdb.set_trace()
    all_tasks = getTaskList()
    for task in all_tasks:
        task.id = task.id + ' '

    if not Player.objects.filter(name=request.user).exists():
        player = Player(name=request.user, tasks_completed=[])
        player.save()
    else:
        player = Player.objects.get(name=request.user)

    context = {
        'title': "Game Page",
        'tasks': all_tasks,
        'player': player
    }

    if request.is_ajax():
        if request.method == 'POST':
            tasks_to_update = request.POST.getlist('toSubmit[]')
            for task in tasks_to_update:
                player.tasks_completed.append(task)
            player.save()
            context['player'] = player
            return redirect(reverse('game:index'))

    # for i in range(0, len(player.tasks_completed)):
    #     player.tasks_completed[i] = player.tasks_completed[i][:-1]
    # context['player'] = player

    return render(request, 'game/game.html', context)

@login_required()
def gameRules(request):
    if not Player.objects.filter(name=request.user).exists():
        player = Player(name=request.user, tasks_completed=[])
        player.save()
    else:
        player = Player.objects.get(name=request.user)
        player.tasks_completed = []
        player.save()

    context = {
        'title': "Game Rules Page"
    }

    return render(request, 'game/gameRules.html', context)
