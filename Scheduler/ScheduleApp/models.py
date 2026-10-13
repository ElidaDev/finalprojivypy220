from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(unique=True,primary_key=True, null=False)
    firstName = models.CharField(max_length=25, null=False)
    lastName = models.CharField(max_length=25, null=False)
    position = models.CharField(max_length=25, null=False)
    email = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class Shift(models.Model):
    id = models.IntegerField(unique=True,primary_key=True, null=False)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=False
    )    
    startDateTime = models.DateTimeField(default=timezone.now, null=False)
    endDateTime = models.DateTimeField(default=timezone.now, null=False)
    
    def __str__(self):
            return f"{self.employee.firstName} {self.startDateTime.strftime("%x %I:%M %p")} -> {self.endDateTime.strftime("%x %I:%M %p")}"
    
class Event(models.Model):
    id = models.IntegerField(unique=True,primary_key=True, null=False)
    shift = models.ForeignKey(
        Shift,
        on_delete=models.CASCADE, null=False
    )    
    name = models.CharField(max_length=25, null=False)
    startDateTime = models.DateTimeField(default=timezone.now, null=False)
    endDateTime = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
            return f"{self.name} {self.startDateTime.strftime("%x %I:%M %p")} -> {self.endDateTime.strftime("%x %I:%M %p")}"
        