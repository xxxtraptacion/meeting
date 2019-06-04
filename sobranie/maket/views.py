from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from .forms import *
from django.views.generic import View
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm


def meetings_list(request):
    col_list = Collect.objects.all()
    context = {'col_list': col_list}
    return render(request, 'maket/meetings.html', context)


def reg_in_bd_user(request):
    if request.method == "POST":
        if request.POST['inputPassword'] == request.POST['inputPassword2']:
            user = Userpr(username=request.POST['inputLogin'], password=request.POST['inputPassword'])
            user.save()
            return HttpResponseRedirect('/maket/meetings/')


def general_meetings_list(request):
    return render(request, 'maket/general_meetings.html')


def create_meeting(request):
    return render(request, 'maket/create_meeting.html')


def my_meetings_list(request):
    return render(request, 'maket/my_meetings.html')


def vote_meeting(request):
    return render(request, 'maket/vote_meeting.html')


def private_meetings_list(request):
    return render(request, 'maket/private_meetings.html')



