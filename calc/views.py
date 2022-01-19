import csv

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import DestinationForm
from .models import Destination
from django.http import HttpResponse

# Create your views here.

def home(request):
    form = DestinationForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "home.html", {'form' : form})  


def show(request):
   destination = Destination.objects.all()
   return render (request, 'show.html', {'destination': destination})

def update(request, id):
   destination = Destination.objects.get(id=id)
   form = DestinationForm(request.POST, instance = destination)
   if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
   return render(request, 'update.html', {'destination' : destination})   


def delete(request, id):
   form = Destination.objects.get(id=id)
   form.delete()
   return HttpResponseRedirect('/')


def export(request):

    destination = Destination.objects.all()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = "inventory.csv"' 

    writer = csv.writer(response)
    writer.writerow(['product_name', 'price', 'quantity'])

    for dest in destination:
        writer.writerow([dest.product_name, dest.price, dest.quantity])

    return response  


