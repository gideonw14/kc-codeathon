import json
import random

if __name__ == "__main__":
	with open("tasks.json") as task_file:
		d = json.loads(task_file.read())
	usedIds = list()
	