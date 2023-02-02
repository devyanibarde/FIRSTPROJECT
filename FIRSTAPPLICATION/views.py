from django.shortcuts import render
from django.http import HttpResponse
from FIRSTAPPLICATION.forms import *
from FIRSTAPPLICATION.models import *

# Create your views here.
def index(request):
    return render(request, 'FIRSTAPPLICATION/index.html')

def showForm(request):
    af = AddPersonForm()
    if request.method == "POST":
        formdata = AddPersonForm(request.POST)
        if formdata.is_valid():
            formdata.save()
    return render(request, "FIRSTAPPLICATION/AddPerson.html", context={"p":af})

def showdata(request):
    data = Person.objects.all()
    return render(request, "FIRSTAPPLICATION/showdata.html", context={'data':data})