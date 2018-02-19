# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Videos
class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4.hex[:8], editable=False)

    video_link = models.TextField(verbose_name='video_link', max_length=1000, help_text='Insert video link here')

    happiness = models.IntegerField(verbose_name='e_happiness', default=0)
    sadness = models.IntegerField(verbose_name='e_sadness', default=0)
    disgust = models.IntegerField(verbose_name='e_disgust', default=0)
    anger = models.IntegerField(verbose_name='e_anger', default=0)
    surprise = models.IntegerField(verbose_name='e_surprise', default=0)

    date_shared = models.DateField(blank=False)

    total_views = models.IntegerField(verbose_name='total_views', default=0)

    user_id = models.ForeignKey('User', on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-date_shared"]

    def __str__(self):
        return self.video_link

# Users
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4.hex[:8], editable=False)

    username = models.CharField(max_length=50)

    # TO-DO: figure out how to use encryption to store passwords

    happiness = models.IntegerField(verbose_name='e_happiness', default=0)
    sadness = models.IntegerField(verbose_name='e_sadness', default=0)
    disgust = models.IntegerField(verbose_name='e_disgust', default=0)
    anger = models.IntegerField(verbose_name='e_anger', default=0)
    surprise = models.IntegerField(verbose_name='e_surprise', default=0)

# Emotions for certain videos
class VideoToUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4.hex[:8], editable=False)

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    video_id = models.ForeignKey(Video, on_delete=models.SET_NULL)

    happiness = models.IntegerField(verbose_name='e_happiness', default=0)
    sadness = models.IntegerField(verbose_name='e_sadness', default=0)
    disgust = models.IntegerField(verbose_name='e_disgust', default=0)
    anger = models.IntegerField(verbose_name='e_anger', default=0)
    surprise = models.IntegerField(verbose_name='e_surprise', default=0)

    
