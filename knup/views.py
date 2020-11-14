from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import File
from .serializers import FileSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def index(request):
    return HttpResponse('asd')

@csrf_exempt
def file_index(request):
    if request.method == 'GET':
        query_set = File.objects.all()
        serializer = FileSerializer(query_set, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FileSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def file_test(request, userid):
    return HttpResponse(userid)