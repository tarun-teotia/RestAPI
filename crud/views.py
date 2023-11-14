# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item, Item2
from .serializers import ItemSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/v1/tasks/',
        'specific': '/v1/tasks/<int:pk>/',
        'add': '/v1/tasks/add/',
        'addBulk': '/v1/tasks/addbulk/',
        'update': '/v1/tasks/update/<int:pk>/',
        'delete': '/v1/tasks/delete/<int:pk>/',
        'deleteBulk': '/v1/tasks/delete_bulk/',
    }
    return Response(api_urls)

@api_view(['GET'])
def list_allTasks(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    temp = {}
    temp["tasks"] = []
    for x in serializer.data:
        temp["tasks"].append(x)

    return Response(temp)

@api_view(['GET'])
def specific_task(request, pk):
    try:
        items = Item.objects.get(id=pk)
        serializer = ItemSerializer(items, many=False)
        return Response(serializer.data)
    except:
        temp = {}
        temp["error"] = 'there is no task at that id.'
        return Response(temp, status=404)

@api_view(['POST'])
def add_task(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    temp = {}
    temp["id"] = serializer.data["id"]
    return Response(temp, status=201)

#----------------------------------------------------
@api_view(['POST'])
def addBulk_tasks(request):
    serializer = request.data
    bulk = serializer["tasks"]

    temp2 = {}
    temp2["tasks"] = []
    for x in bulk:
        serializer2 = ItemSerializer(data=x)
        if serializer2.is_valid():
            serializer2.save()
        temp = {}
        temp["id"] = serializer2.data["id"]
        temp2["tasks"].append(temp)

    return Response(temp2, status=201)
#----------------------------------------------------

@api_view(['PUT'])
def update_task(request, pk):
    try:
        items = Item.objects.get(id=pk)
        serializer = ItemSerializer(instance=items, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=204)
    except:
        temp = {}
        temp["error"] = 'there is no task at that id.'
        return Response(temp, status=404)

@api_view(['DELETE'])
def delete_task(request, pk):
    items = Item.objects.get(id=pk)
    items.delete()
    return Response("", status=204)

#----------------------------------------------------
@api_view(['POST'])
def delete_bulkTask(request):
    serializer = request.data
    bulk = serializer["tasks"]

    for x in bulk:
        pk = x["id"]
        items = Item.objects.get(id=pk)
        items.delete()

    return Response("", status=204)
#----------------------------------------------------