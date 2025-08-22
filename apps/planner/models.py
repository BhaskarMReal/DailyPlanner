from ..authentication.models import CustomUser
from django.db import models

class Tasks(models.Model):
    taskid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    date = models.DateField()
    completed = models.BooleanField()
    important = models.BooleanField()

    def __str__(self):
        return self.task