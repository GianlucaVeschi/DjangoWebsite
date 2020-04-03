from django.shortcuts import render
from personal.models import Question
# Create your views here.

def home_screen_view(request):

	#Print headers to the console
	#print(request.headers)
	
	#First way to declare a Context
	#context = {}
	#context['some_string'] = "GIANLUCA"

	#Second way to declare a Context
	#context = {
	#	'some_string' : "this is a string i'm passing to the view, I hope it works",
	#	'some_number' : 123456,
	#}

	#How to Declare a list
	#context = {}
	#list_of_values = []
	#list_of_values.append("This are")
	#list_of_values.append("the values")
	#list_of_values.append("of the")
	#list_of_values.append("list of values")

	#context['list_of_values'] = list_of_values

	context = {}
	questions = Question.objects.all()
	context['questions'] = questions


	return render(request, "personal/home.html", context)


