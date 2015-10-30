from django.shortcuts import render
from main.models import Person

def myview(request):
	peeps = Person.objects.all()
	return render(request, 'home.html', {'peeps':peeps})
