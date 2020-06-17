from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from outset.models import UserDetail


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    user_detail = UserDetail.objects.get(auth_user=user)
    print("Fetched User:", user_detail.__str__())
    return render(request,
                  "outset/profile.html",
                  {'user_detail' : user_detail})
