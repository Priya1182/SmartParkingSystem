from django.forms.models import inlineformset_factory
from django import forms
from parking import models
from parking.models import Park, Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class creatparkingslotFrom(forms.ModelForm):

# 	date = models.DateField()
# 	location = models.CharField(max_length=20,default=None)
# 	slot_type = models.CharField(max_length=20,default=None)
# 	slots  = models.IntegerField()
	

		
		
# 	class Meta():
# 		"""docstring for Meta"""
# 		model = Park
# 		fields = ('date',
# 			      'location ',
# 			      'slots',)

# class ParkForm(forms.ModelForm):  
#     class Meta:  
#         model = Park  
#         fields = "__all__"  

