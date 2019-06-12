from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import *
from django.views.generic import View
from .models import *
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm


def meetings_list(request):
    return redirect('/maket/public_meetings/')


def public_meetings_list(request):
    publicMeet = Collect.objects.filter(tpesobr="Общедоступное")
    publicMeet=publicMeet[::-1]
    context = {'publicMeet': publicMeet}
    return render(request, 'maket/public_meetings.html', context)


def create_meeting(request):
    users = User.objects.all()
    context = {'users': users}
    if request.method == 'POST':
        collect = Collect()
        listUsers = request.POST.getlist('selectUsers')
        if listUsers:
            collect.tpesobr = "Приватное"
        collect.name = request.POST.get('collectName')
        collect.description = request.POST.get('collectDescription')
        collect.theme = request.POST.get('collectTheme')
        collect.user = request.user
        collect.duration = request.POST.get('timepickerDuration')
        collect.save()
        if listUsers:
            for user in listUsers:
                userincollect = UserInCollect()
                useru = User.objects.get(username=user)
                userincollect.user = useru
                userincollect.collect = Collect.objects.get(name=collect.name)
                userincollect.save()
        timelist = request.POST.getlist('time[]')
        datelist = request.POST.getlist('date[]')
        if timelist:
            for time in timelist:
                timecollect = TimeCollect()
                timecollect.collect = Collect.objects.get(name=collect.name)
                timecollect.time = time
                timecollect.save()
        if datelist:
            for date in datelist:
                datecollect = DateCollect()
                datecollect.collect = Collect.objects.get(name=collect.name)
                datecollect.date = date
                datecollect.save()
        return redirect('/maket/public_meetings/')
    return render(request, 'maket/create_meeting.html', context)


def my_meetings_list(request):
    my_meets_list = Collect.objects.filter(user__username=request.user.username)
    my_meets_list = my_meets_list[::-1]
    context = {'my_meets_list': my_meets_list}
    return render(request, 'maket/my_meetings.html', context)


def vote_meeting(request, meeting_slug):
    votes = {}
    collect = Collect.objects.get(slug=meeting_slug)
    date_list = DateCollect.objects.filter(collect__name=collect.name)
    time_list = TimeCollect.objects.filter(collect__name=collect.name)
    vote_list = Golos.objects.filter(collect__name=collect.name)
    #for date in date_list:
     #   for time in time_list:
      #      votes[str((date.date, time.time))] = len(vote_list.filter(time__time=time.time).filter(date__date=date.date))
    context = {'collect': collect, 'date_list': date_list, 'time_list': time_list, 'votes': votes}
    return render(request, 'maket/vote_meeting.html', context)


def private_meetings_list(request):
    private_list = Collect.objects.filter(tpesobr="Приватное")
    private_colls = private_list.filter(userincollect__user__username__contains=request.user.username)
    private_colls = private_colls[::-1]
    context = {'private_colls': private_colls}
    return render(request, 'maket/private_meetings.html', context)


def delete(request, name):
    try:
        collect = Collect.objects.get(name=name)
        collect.delete()
        return redirect('/maket/my_meetings/')
    except Collect.DoesNotExist:
        return redirect('/maket/my_meetings/')
