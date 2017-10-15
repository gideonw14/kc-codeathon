import json
import uuid

if __name__ == "__main__":
	with open("tasks.json", "r") as task_file:
		d = json.loads(task_file.read())

	for i, task in enumerate(d["tasks"]):
		d["tasks"][i]["id"] = str(uuid.uuid4())

	with open("tasks.json", "w") as task_file:
		json.dump(d, task_file, sort_keys=False, indent=4)


