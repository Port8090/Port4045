from django.shortcuts import redirect, render, get_object_or_404
from .forms import imageForm
from django.http import HttpResponse

# from . import models
# from .models import Question

# Create your views here.

def index(request):
    form = imageForm()
    return render(request, 'index.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            context = {'image_url': 'images/image3863.jpg'}
            return render(request, 'result.html', context)
    else:
        form = imageForm()
    return redirect('foodpic')
