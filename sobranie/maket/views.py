from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import *
from django.views.generic import View
from .models import *
from django.template import Context
from django.utils.text import slugify
from collections import defaultdict
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm


def public_meetings_list(request):
    publicMeet = Collect.objects.filter(tpesobr="Общедоступное")
    publicMeet =publicMeet[::-1]
    context = {'publicMeet': publicMeet}
    return render(request, 'maket/public_meetings.html', context)


def create_meeting(request):
    users = User.objects.all()
    context = {'users': users}
    if request.method == 'POST':
        collect = Collect()
        listUsers = request.POST.getlist('selectUsers')
        if listUsers:
            collect.tpesobr = "По приглашению"
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
    collect = Collect.objects.get(slug=meeting_slug)
    date_list = DateCollect.objects.filter(collect__name=collect.name)
    time_list = TimeCollect.objects.filter(collect__name=collect.name)
    vote_list = Golos.objects.filter(collect__slug=collect.slug)
    if request.method == 'POST':
        golos = Golos()
        useru = User.objects.get(username=request.user.username)
        time = request.POST.get('votetime')
        date = request.POST.get('votedate')
        golosindb = Golos.objects.filter(collect__slug=meeting_slug).filter(user=useru).filter(time__time=time).filter(date__date=date)
        if golosindb:
            golosindb.delete()
        else:
            golos.collect = Collect.objects.get(slug=meeting_slug)
            golos.user = useru
            golos.time = TimeCollect.objects.filter(collect__slug=meeting_slug).get(time=time)
            golos.date = DateCollect.objects.filter(collect__slug=meeting_slug).get(date=date)
            golos.save()
    date_list_1 = [date.id for date in date_list]
    time_list_1 = [time.id for time in time_list]
    votes = []
    for date in date_list:
        tmp = []
        for time in time_list:
            tmp.append({
                "count": len(vote_list.filter(time__time=time.time).filter(date__date=date.date)),
                "date": date,
                "time": time,
            })
        votes.append(tmp)
    context = {
        'collect': collect,
        'date_list': date_list,
        'time_list': time_list,
        'votes': votes,
        'time_list_1': time_list_1,
        'date_list_1': date_list_1,
    }
    return render(request, 'maket/vote_meeting.html', context)


def private_meetings_list(request):
    private_list = Collect.objects.filter(tpesobr="По приглашению")
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
