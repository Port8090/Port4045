from django.shortcuts import redirect, render
from .forms import imageForm
# Create your views here.



def index(request):
    form = imageForm()
    return render(request, 'index.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('foodpic:index')
    else:
        form = imageForm()
    return redirect('foodpic')
