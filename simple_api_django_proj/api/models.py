from django.db import models

class TaskModel(models.Model):
    Id = models.AutoField(primary_key=True)
    Checked = models.BooleanField()
    Name = models.CharField(max_length=400)
    Type = models.CharField(max_length=400)
    Age = models.BigIntegerField()
    Description = models.CharField(max_length=400)
    Date = models.DateTimeField(auto_now_add=True)