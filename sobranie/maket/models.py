from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
import datetime


class Collect(models.Model):  # Собрание
    name = models.CharField('Название собрания', max_length=100, db_index=True,primary_key=True)
    tpesobr = models.CharField('Тип собрания',max_length= 20,default='Общедоступное')
    user = models.ForeignKey(User,verbose_name='Организатор',on_delete=models.CASCADE,unique=False)
    theme = models.CharField('Тема собрания', max_length=250)
    description = models.CharField('Описание собрания',max_length=500)
    duration = models.TimeField(verbose_name='Длительность')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vote_meeting_url', kwargs={'meeting_slug': self.slug})


def pre_save_collect_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name, allow_unicode=True)
        instance.slug = slug


pre_save.connect(pre_save_collect_slug, sender=Collect)


class UserInCollect(models.Model):
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    collect = models.ManyToManyField(Collect)


class DateCollect (models.Model):
    collect = models.ForeignKey(Collect,verbose_name='Собрание',on_delete=models.CASCADE,unique=False)
    date = models.DateField(verbose_name='Дата')


class TimeCollect (models.Model):
    collect = models.ForeignKey(Collect,verbose_name='Собрание',on_delete=models.CASCADE,unique=False)
    time = models.TimeField(verbose_name='Время')


class Golos(models.Model):
    collect = models.ForeignKey(Collect,verbose_name='Собрание',on_delete=models.CASCADE,unique=False)
    user = models.ForeignKey(User,verbose_name='Пользователь',related_name='up',on_delete=models.CASCADE)
    date =models.ForeignKey(DateCollect, verbose_name='Дата',on_delete=models.CASCADE)
    time = models.ForeignKey(TimeCollect, verbose_name='Время',on_delete=models.CASCADE)