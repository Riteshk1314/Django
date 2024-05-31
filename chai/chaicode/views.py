from django.shortcuts import render
from .models import ChaiVariety

def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'chai/all_chai.html', {'chais': chais})