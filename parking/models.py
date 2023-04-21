from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User,auth
from django import forms

# Create your models here.
class Park(models.Model):
	parkid = models.CharField(max_length=10,default=None)
	park_name = models.CharField(max_length=20,default=None)
	park_location = models.CharField(max_length=20,default=None)
	slot_type = models.CharField(max_length=20,default=None)
	date = models.DateField()
	slotsNo  = models.IntegerField()

	def __str__(self):
		return str(self.date)



class Book(models.Model):
	#user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	vehicle_no = models.CharField(max_length=8,default=None)
	start_time = models.TimeField(default=None)
	end_time = models.TimeField(default=None)
	park_name = models.CharField(max_length=20,default=None)
	park_location = models.CharField(max_length=20,default=None)
	slot_type = models.CharField(max_length=20,default=None)
	#Date 
	
