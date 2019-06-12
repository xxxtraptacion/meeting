from django.urls import path,include
from .views import *

urlpatterns = [
    path('public_meetings/', public_meetings_list, name='public_meetings_list_url'),
    path('private_meetings/', private_meetings_list, name='private_meetings_list_url'),
    path('create_meeting/', create_meeting, name='create_meeting_url'),
    path('my_meetings/', my_meetings_list, name='my_meetings_list_url'),
    path('vote_meeting/<meeting_slug>/', vote_meeting, name='vote_meeting_url'),
    path('accounts/', include('allauth.urls')),
    path('my_meetings/delete/<str:name>/', delete),

]
