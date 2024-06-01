from django.shortcuts import render
from .models import ChaiVariety

def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'website/all_chai.html', {'chais': chais})

from django.shortcuts import render, get_object_or_404

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'website/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    return render(request, 'website/chai_stores.html')