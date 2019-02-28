from django.urls import path
from .views import *

urlpatterns = [
    path('meetings/', meetings_list, name='meetings_list_url'),
    path('general_meetings/', general_meetings_list, name='general_meetings_list_url'),
    path('create_meeting/', create_meeting, name='create_meeting_url'),
    path('my_meetings/', my_meetings_list, name='my_meetings_list_url'),
    path('template_directory/', template_directory_list, name='template_directory_list_url'),

]
