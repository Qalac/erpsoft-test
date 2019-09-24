from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *

def index(request):
    template_name = 'home.html'
    return render(request, template_name)

def list_object(request):
    query = Human.objects.all()
    return render(request, 'list.html', {'query': query})

def create_object(request):    
    if request.method=='POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('SUCCESSFULLY SAVED INFO')
    else:
        form = HumanForm()
    return render(request,'form.html', {'form': form})

# Create your views here.
