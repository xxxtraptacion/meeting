from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):

    class Meta:
        model = Userpr
        fields = ("username", "password",)
