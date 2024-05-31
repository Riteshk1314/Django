from django.shortcuts import render

def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'chai/all_chai.html', {'chais': chais})