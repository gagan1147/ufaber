from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=10,null=False, blank=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=100)
    start_time = models.CharField(max_length=200)
    end_time =  models.CharField(max_length=200)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title


