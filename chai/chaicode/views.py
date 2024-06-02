from django.shortcuts import render
from .models import ChaiVariety, store #getting models 
from .forms import ChaiVarietyForm #importing forms
def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'website/all_chai.html', {'chais': chais})

from django.shortcuts import render, get_object_or_404

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'website/chai_detail.html', {'chai': chai})


def chai_store_view(request):
    stores=None
    if request.method== 'POST':
        form=ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores=store.object.filter(chai_varieties=chai_variety)
        
    else:
        form=ChaiVarietyForm()
        
    
    return render(request, 'website/chai_stores.html',{'stores':stores,'form':form})