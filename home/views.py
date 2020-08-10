from django.shortcuts import render
from datetime import date
from home.models import student

# Create your views here.
def ho(request):
    students=student.objects.all()
    return render(request, 'home/home.html', {'students': students})