from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from django.views.generic import View
from .models import *
from django.contrib.auth import login,logout


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


def template_directory_list(request):
    return render(request, 'maket/template_directory.html')


def vote_meeting(request):
    return render(request, 'maket/vote_meeting.html')


def edit_profile(request):
    return render(request, 'maket/edit_users_profile.html')


def create_template(request):
    return render(request, 'maket/create_template.html')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("maket/meetings.html")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = RegisterForm()
    return render(request, 'maket/register.html', context={"form": form})


def login_user(request):
    return render(request, 'maket/login.html')


def private_meetings_list(request):
    return render(request, 'maket/private_meetings.html')


def create_meeting_from_template(request):
    return render(request, 'maket/create_meet_from_template.html')


def my_template_directory(request):
    return render(request, 'maket/my_template_directory.html')




