from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from .models import Video
from .filters import *
import datetime

def index(request):
    return render(request, 'index.html', {})

def video_content(request):
    return render(request, 'video-content.html', {})

def user_profile(request):
    return render(request, 'user-profile.html', {})

def login_page(request):
    return render(request, 'login.html', {})

def signup_page(request):
    return render(request, 'signup.html', {})

def upload_page(request):
    return render(request, 'upload.html', {})

def search_page(request):
    return render(request, 'search-results.html', {})

def explore_page(request):
    # get list of new videos
    new_cutoff = datetime.datetime.now() - datetime.timedelta(days=7)
    new_videos = Video.objects.filter(date_shared__gte=new_cutoff)

    # get list of popular videos
    popular_videos = Video.objects.all()
    # get list of controversial videos?
    return render(
        request,
        'explore.html',
        context={
            "new_videos":new_videos,
            "popular_videos":popular_videos,
        },
    )
