from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
import json
import os


def getTaskList():
	all_tasks = list()
	with open("game/tasks.json","r") as json_file:
		json_dict = json.loads(json_file.read())
	for task_data in json_dict["tasks"]:
		all_tasks.append(Task(task_data))
	return all_tasks


def game(request):
    # tasks = Task.objects.all()
    all_tasks = getTaskList()
  

    context = {
        'title': "Game Page",
        'tasks': all_tasks,
    }
    return render(request, 'game/game.html', context)

if __name__ == "__main__":
	d = getTaskList()
	print(d)
