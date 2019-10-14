from django.shortcuts import render
from django.http import HttpResponse
from .models import Telefonbucheintrag

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def einträge(request):
    einträge = Telefonbucheintrag.objects.all()
    return render(request, 'einträge.html', context= {'einträge': einträge})

def test():
    return "Test"
