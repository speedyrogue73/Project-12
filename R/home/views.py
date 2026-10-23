
from django.http import HttpResponse
from django.shortcuts import render
from.models import Reza

def home(request):
    Rezas = Reza.objects.all()
    return render(request, template_name= 'home/landing.html' , context={'Rezas':Rezas})