from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from outset.models import UserDetail


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    absurl = UserDetail.get_absolute_url(user.user_detail)
    print(absurl)
    return render(request,
                  "outset/profile.html",
                  {'user' : user})
