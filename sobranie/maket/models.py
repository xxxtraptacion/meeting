from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime


class Userpr(models.Model):
    username = models.CharField('username',max_length=150,unique=True,db_index=True)
    password = models.CharField('password',db_index=True,max_length=120)
    email = models.EmailField('Email',unique=True,max_length=150)

    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username


class Moment (models.Model):
    nazv = models.CharField('nazv',max_length=100,db_index=True)
    duration = models.TimeField(auto_now_add=False)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.nazv


class Template(models.Model): #Шаблон собрания
    namet = models.CharField('namet',max_length=100,unique=True,db_index=True)
    theme = models.CharField('theme',max_length=250,db_index=True)
    leading = models.CharField('lead',max_length=50) #Ведущий собрания. Т.К это шаблон здесь ведущего определит система.
    datetime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.namet


class Golos(models.Model):
    username = models.CharField('username',max_length=100,db_index=True)
    flag= models.BooleanField('flag',default=False)
    timemomenst = models.OneToOneField(Moment,on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Collect(models.Model):  # Собрание
    name = models.CharField('name', max_length=100, db_index=True)
    data = models.DateTimeField('data', auto_now_add=True)
    org = models.CharField('org', max_length=70, unique=True)
    man = models.CharField('man', max_length=50 )
    theme = models.CharField('theme', max_length=250)
    peopleincoll = models.ForeignKey(Golos,on_delete=models.CASCADE,related_name='peopleincoll')

    def __str__(self):
        return self.name


class RequiredPeople(models.Model):
    namesobr = models.ManyToManyField(Collect)
    listeners = models.ForeignKey(Collect,on_delete=models.CASCADE,related_name='listeners')
    leading = models.ForeignKey(Collect,on_delete=models.CASCADE,related_name='leading')
