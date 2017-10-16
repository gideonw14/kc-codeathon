from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task, Player
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.contrib.auth.decorators import login_required
import os.path

def getTaskList(username):
	all_tasks = list()
	if os.path.exists("game/saves/" + username + ".json"):
	# if False:
		json_file = open("game/saves/" + username + ".json","r")
	else:
		json_file = open("game/tasks.json","r")
	json_dict = json.loads(json_file.read())
	json_file.close()
	for task_data in json_dict["tasks"]:
		all_tasks.append(Task(task_data))
	return all_tasks

def saveTasks(completed, taskList, username):
	print(taskList)
	for i, task in enumerate(taskList):
		taskList[i] = task.__dict__
	for i, task in enumerate(taskList):
		if "{} ".format(task["id"]) in completed or task["id"] in completed:
			taskList[i]["completed"] = True
	with open("game/saves/" + username + ".json", "w") as json_file:
		json.dump({"tasks" : taskList}, json_file, sort_keys=False, indent=4)


@login_required()
@csrf_exempt
def game(request):
	all_tasks = getTaskList(request.user.username)

	if not Player.objects.filter(name=request.user).exists():
		player = Player(name=request.user, tasks_completed=[])
		player.save()
	else:
		player = Player.objects.get(name=request.user)

	context = {
		'title': "Game Page",
		'tasks': all_tasks,
	}

	if request.is_ajax():
		if request.method == 'POST':
			tasks_to_update = request.POST.getlist('toSubmit[]')
			saveTasks(tasks_to_update, all_tasks, request.user.username)

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
