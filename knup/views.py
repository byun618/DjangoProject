from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import File
from .serializers import FileSerializer
from .forms import UploadForm

# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html', {})

def image_list(request):
    return render(request, 'list.html', {})

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        print(request.FILES)
        if form.is_valid():
            
            upload_file = form.save(commit=False) 
            upload_file.filename = 'asd'
            upload_file.save() 

            # form.save()

            return redirect('knup:image_list')

    else:
        form = UploadForm()

    return render(request, 'upload.html', {
        'form': form
    })


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