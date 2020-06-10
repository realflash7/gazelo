from django.http import HttpResponse
from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    else:
        return HttpResponse("Hey, guys!!")