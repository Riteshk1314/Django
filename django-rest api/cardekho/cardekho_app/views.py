from django.shortcuts import render
from .models import carlist
from django.http import JsonResponse
from django.http import HttpResponse
import json
from .serializers import carserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# def car_list_view(request):
#     cars=carlist.objects.all()
#     data={
#         'cars':list(cars.values()),
        
#     }
#     data_json=json.dumps(data)
#     return HttpResponse(data_json, content_type='application/json' )

# def car_detail_view(request,pk):
    
#     car=carlist.objects.get(pk=pk)
#     data={
#         'name':car.name,
#         'descrption':car.description,
#         'active':car.active,
        
        
#     }
#     return JsonResponse(data)

@api_view(['GET','POST'])
def car_list_view(request):
    if request.method=='GET':
        car=carlist.objects.all()
        serializer=carserializer(car,many=True)
        return Response(serializer.data)
    
    
    if request.method=='POST':
        serializer=carserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        

@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    
    if request.method=='GET':
        car=carlist.objects.get(pk=pk)
        serializer=carserializer(car)
        serializer_data=serializer.data
        return Response(serializer_data)
    
    if request.method=='PUT':
        try:
            
            car=carlist.objects.get(pk=pk)
        except:
            return Response({'error':'car not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=carserializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data=serializer.data
            return Response(serializer_data)
        
        else:
            return Response(serializer.errors)
        
    if request.method=='DELETE':
        car=carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=202)
        
    
