from django.shortcuts import render
from django.http import HttpResponse
from FIRSTAPPLICATION.forms import *

# Create your views here.
def index(request):
    return render(request, 'FIRSTAPPLICATION/index.html')

def showForm(request):
    af = AddPersonForm()
    return render(request, "FIRSTAPPLICATION/AddPerson.html", context={"p":af})