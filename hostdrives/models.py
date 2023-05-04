from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class websiteUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    hosted=models.IntegerField(blank=True)
    attended=models.IntegerField(blank=True)
    
class drive(models.Model):
    organizer=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateTimeField()
    description=models.TextField()
    location=models.CharField(max_length=255)
    attendees=models.ManyToManyField(User,related_name='attending_events',null=True)
    def __str__(self):
        return self.name


