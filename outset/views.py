from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request,
                  "outset/profile.html",
                  {'user' : user})
