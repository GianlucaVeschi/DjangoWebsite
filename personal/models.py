from django.db import models

# Create your models here.

PRIORITY = [	#tuple of priorities
	("H", "High"),
	("M", "Medium"),
	("L", "Low"),
] 

class Question(models.Model):
	title 					= models.CharField(max_length=60) #CharField,TextField = Django Data types 
	question 				= models.TextField(max_length=400)
	priority 				= models.CharField(max_length=1, choices=PRIORITY)

	"""toString() method"""
	def __str__(self):
		return self.title
		

	class Meta:
		verbose_name = "Question"				#Name in the row
		verbose_name_plural = "Users Question"	#Name in the Home