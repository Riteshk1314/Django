from django.http import HttpResponse
from django.shortcuts import render

def all_chai(request):
    return render(request, 'website/all_chai.html')
def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")