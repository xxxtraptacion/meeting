from django.urls import path
from .views import *

urlpatterns = [
    path('meetings/', meetings_list, name='meetings_list_url'),
    path('general_meetings/', general_meetings_list, name='general_meetings_list_url'),
    path('private_meetings/', private_meetings_list, name='private_meetings_list_url'),
    path('create_meeting/', create_meeting, name='create_meeting_url'),
    path('create_meeting_from_template/', create_meeting_from_template, name='create_meeting_from_template_url'),
    path('my_meetings/', my_meetings_list, name='my_meetings_list_url'),
    path('template_directory/', template_directory_list, name='template_directory_list_url'),
    path('vote_meeting/', vote_meeting, name='vote_meeting_url'),
    path('edit_profile/', edit_profile, name='edit_profile_url'),
    path('create_template/', create_template, name='create_template_url'),
    path('register/', register_user, name='register_url'),
    path('login/', login_user, name='login_url'),

]
