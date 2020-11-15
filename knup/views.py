from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from rest_framework.parsers import JSONParser

from .models import File
from .serializers import FileSerializer
from .forms import UploadForm


from pathlib import Path
import os

from django.contrib.auth.hashers import make_password, is_password_usable

# Create your views here.

@csrf_exempt
def index(request):
    
    return render(request, 'index.html', {})

@csrf_exempt
def file_list(request):

    query_set = File.objects.all().filter(userid=12345)
    serializer = FileSerializer(query_set, many=True)

    # return JsonResponse(serializer.data, safe=False)
    return render(request, 'list.html', {
        'data': serializer.data
    })

@csrf_exempt
def file_preview(request):

    file_name = request.POST['file']
    p, fn = os.path.split(file_name)
    file_path = os.path.join(settings.MEDIA_ROOT, fn)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            res = HttpResponse(fh.read(), content_type="application/pdf")
            return res

@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        files = request.FILES.getlist('storedname')

        if form.is_valid():
            
            for idx, f in enumerate(files):
                
                originalname = f.name
                storedname = make_password(f.name)
                print(storedname)
                f.name = storedname

                file_instance = File(originalname=originalname, storedname=f, userid=12345)
                file_instance.save()

            return redirect('knup:file_list')

    else:
        form = UploadForm()

    return render(request, 'upload.html', {
        'form': form
    })

