from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from . import constants as c

# Create your models here.

# class Task(models.Model):
#     name = models.CharField(max_length=c.TASK_NAME_MAX)
#     prerequisites = ArrayField(models.CharField(max_length=c.TASK_NAME_MAX))
#     delay = models.IntegerField(default=0)
#     time_to_complete = models.IntegerField()
#     category = models.CharField(max_length=c.TASK_CATEGORY_MAX)

#     def __str__(self):
#         return self.name

class Player(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    knowledge = models.ManyToManyField('Knowledge')
    tasks_completed = ArrayField(models.CharField(max_length=c.TASK_NAME_MAX))

    def __str__(self):
        return self.name

class Knowledge(models.Model):
    category = models.CharField(max_length=c.TASK_CATEGORY_MAX)
    proficiency = models.FloatField(default=1.0)

    def __str__(self):
        return self.category

class Task():
    def __init__(self, data):
        """data must be a dictionary"""
        self.name = data["name"]
        self.prerequisites = data["prerequisites"]
        self.delay = data["delay"]
        self.time_to_complete = data["time_to_complete"]
        self.category = data["category"]
        self.id = data["id"]
        self.completed = data["completed"]

    # def __str__(self):
    #     return self.name
