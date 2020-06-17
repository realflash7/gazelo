from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request,
                  "outset/profile.html",
                  {'user' : user})
