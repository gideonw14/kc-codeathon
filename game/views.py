from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
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
def game(request):
    if request.method == "POST":
        print("\n\n\n", request.POST.getlist('toSubmit[]'))
    # tasks = Task.objects.all()
    all_tasks = getTaskList()

    context = {
        'title': "Game Page",
        'tasks': all_tasks,
    }
    return render(request, 'game/game.html', context)

def gameRules(request):
    context = {
        'title': "Game Rules Page"
    }

    return render(request, 'game/gameRules.html', context)
