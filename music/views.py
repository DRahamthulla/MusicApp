from asyncio import exceptions
from cmath import e
from functools import cache
import os
from pyexpat.errors import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.urls import reverse
from  .models import MusicFile
from .forms import MusicFileForm,RegistrationForm
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
import magic
from django.conf import settings
User = settings.AUTH_USER_MODEL

import sys
sys.setrecursionlimit(1500)

def home_view(request):
    return render(request, 'base.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music:login')
    else:
        form =RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        if form.is_valid():
            user=form.get_user()
        login(request,user)
        return redirect(reverse('music:back'))
    else:
        form = AuthenticationForm()
    return form

def user_logout(request):
    logout(request)
    return render(request, 'base.html')



def upload_view(request, value):
    if request.method == 'POST':
     form = MusicFileForm(request.POST, request.FILES)
     if form.is_valid():
        file = request.FILES['file']
        value = form.cleaned_data['value']
        file_type = magic.from_buffer(file.read(), mime=True)
        if not file_type.startswith('audio/') and not file_type.startswith('video/'):
            error_message ="only allow the mp3 "
            return render(request, 'exc.html', {'form': form, 'error_message': error_message})    
        #music_file = MusicFile.objects.create(file=file, value=value ,uploaded_by=request.user)
        music_file = form.save(commit=False)
        music_file.uploaded_by = request.user
        music_file.save()    
        return redirect('music:music_files1')
    else:
        form = MusicFileForm()
    
    return render(request, 'upload.html', {'form': form})



def music_files_view(request):
    music_files1= MusicFile.objects.all()
    return render(request, 'music_files.html', {'music_files1':music_files1})

from django.core.paginator import Paginator


def music_player(request):
     music_files1= MusicFile.objects.all()
     return render(request, 'music_player.html', {'music_files2':music_files1})

    
    


def music_search_view(request):
    try:
        query = request.POST.get('query', '')
        music_results = MusicFile.search_by_title(query)
        return render(request, 'search_results.html', {'results': music_results, 'query': query})
    except exceptions as e:
        return render(request, 'exc.html', {'error': str(e)})





