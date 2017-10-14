from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from . import constants as c

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=c.TASK_NAME_MAX)
    prerequisites = ArrayField(models.CharField(max_length=c.TASK_NAME_MAX))
    delay = models.IntegerField(default=0)
    time_to_complete = models.IntegerField()
    category = models.CharField(max_length=c.TASK_CATEGORY_MAX)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    design_knowledge = models.FloatField(default=1.0)
    financial_knowledge = models.FloatField(default=1.0)
    safety_knowledge = models.FloatField(default=1.0)
    build_knowledge = models.FloatField(default=1.0)

    def __str__(self):
        return self.name