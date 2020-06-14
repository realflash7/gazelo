from django.http import HttpResponse
from django.shortcuts import render, redirect

from gazelo.settings import APP_NAME


def welcome(request):
    if request.user.is_authenticated:
        return redirect('video_stream_home')
    else:
        return render(request, "outset/home.html", {'app_name': APP_NAME})