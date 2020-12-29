from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AnimalFoodForm
from .models import AnimalFood





def add_photo(request, template_name='add_photo.html'):
    form = AnimalFoodForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        # return  HttpResponse("ok saved")
        return redirect('FileCompare:manage_photo')
    return render(request, template_name, {'form':form})


def manage_photo(request, template_name='manage_photo.html'):
    std_data = AnimalFood.objects.all() 
    data = {}
    data['object_list'] = std_data
    return render(request, template_name, data)


def edit_photo(request, pk, template_name='add_photo.html'):
    book= get_object_or_404(AnimalFood, pk=pk)
    form = AnimalFoodForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('FileCompare:manage_photo')
    return render(request, template_name, {'form':form})

def delete_photo(request, pk):
    obj = get_object_or_404(AnimalFood, pk=pk)
    obj.delete()
    return redirect('FileCompare:manage_photo')

def home(request, template_name='home.html'):
    return render(request, template_name)

    
def image_match_static(request, template_name='image_match_static.html'):
    return render(request, template_name)

def image_match_dynamic(request, template_name='image_match_dynamic.html'):
    std_data = AnimalFood.objects.all() 
    data = {}
    data['object_list'] = std_data
    return render(request, template_name, data)


