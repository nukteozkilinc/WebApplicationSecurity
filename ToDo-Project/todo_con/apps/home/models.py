from django.db import models
from turtle import title, update
from venv import create
from django.forms import DateField
from django.contrib.auth.models import User
from django.utils import timezone



class Task(models.Model): #id otomatik oluşuyor
    PRIORITY = (
        ('Low','low'),
        ('Medium','medium'),
        ('High','high'),
    )
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField( max_length=10, choices=PRIORITY)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering=('start_time','end_time')
    def __str__(self):
        return self.title
    
    
    
class Day(models.Model):
    date = models.DateField()
    daily_tasks = models.ManyToManyField(Task)
  
