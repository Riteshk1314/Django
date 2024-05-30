from django.shortcuts import render

def all_chai(request):
    return render(request, 'website/all_chai.html')