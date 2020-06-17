from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from outset.models import UserDetail, Following


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    if user is None:
        return HttpResponseNotFound("hello")
    user_detail = UserDetail.objects.get(auth_user=user)
    print("Fetched User:", user_detail.__str__())
    followers = Following.objects.filter(user=user) # Not sure how efficient this way is. Fix-> 1. Better query 2. Query in chunks when page is scrolled
    followings = Following.objects.filter(follower=user) # Not sure how efficient this way is. Fix-> 1. Better query 2. Query in chunks when page is scrolled
    return render(request,
                  "outset/profile.html",
                  {'user_detail' : user_detail,
                   'followers' : followers,
                   'followings' : followings})
