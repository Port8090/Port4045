from django.shortcuts import redirect, render, get_object_or_404
from .forms import imageForm
from django.http import HttpResponse

# from . import models
# from .models import Question

# Create your views here.

from ultralytics import YOLO

model = YOLO('./yolov8n.pt')

from PIL import Image

def index(request):
    form = imageForm()
    return render(request, 'index.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            r = model.predict(source = form.instance.image.name)[0]
            cls = r.names[int(r.boxes.cls[0])]
            result_image = Image.fromarray(r.plot()).convert('RGB')
            result_image_path = "static/result.jpg"
            result_image.save(result_image_path)
            context = {'classname': cls }
            return render(request, 'result.html', context)
    else:
        form = imageForm()
    return redirect('foodpic')
