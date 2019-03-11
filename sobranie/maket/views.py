from django.shortcuts import render, get_object_or_404
from django.views.generic import View


def meetings_list(request):
    return render(request, 'maket/meetings.html')


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
    return render(request, 'maket/register.html')


def login_user(request):
    return render(request, 'maket/login.html')


def private_meetings_list(request):
    return render(request, 'maket/private_meetings.html')




