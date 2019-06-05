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
    col_list = col_list[::-1]
    context = {'col_list': col_list}
    return render(request, 'maket/meetings.html', context)


def public_meetings_list(request):
    publicMeet = Collect.objects.filter(tpesobr="Общедоступное")
    publicMeet=publicMeet[::-1]
    context = {'publicMeet': publicMeet}
    return render(request, 'maket/public_meetings.html', context)


def create_meeting(request):

    return render(request, 'maket/create_meeting.html')


def my_meetings_list(request):
    my_meets_list = Collect.objects.filter(user__username=request.user.username)
    my_meets_list = my_meets_list[::-1]
    context = {'my_meets_list': my_meets_list}
    return render(request, 'maket/my_meetings.html', context)


def vote_meeting(request, meeting_slug):
    collect = Collect.objects.get(slug=meeting_slug)
    context = {'collect': collect}
    return render(request, 'maket/vote_meeting.html', context)


def private_meetings_list(request):
    private_meets_list=dict()
    try:
        user_list = UserInCollect.objects.get(user__username=request.user.username).collect.all()
    except:
        user_list=None
    if user_list:
        private_meets_list = user_list.filter(tpesobr="Приватное")
    context = {'private_meets_list': private_meets_list}
    return render(request, 'maket/private_meetings.html', context)



