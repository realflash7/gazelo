from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from gazelo.settings import APP_NAME
from outset.models import Content

from .forms import InvitationForm
from .models import Invitation


@login_required
def home(request):
    user_contents = Content.objects.contents_added_by_user(
        user=request.user
    )
    all_contents = Content.objects.viewable_contents(
        user=request.user
    )
    print("NEW REQUEST by : ", request.user)
    return render(request, "video_stream/home.html",
            {'app_name': APP_NAME, 'ncontents': Content.objects.count(), 'my_contents': user_contents, 'all_contents': all_contents})


@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user = request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_stream_home')
    else:
        form = InvitationForm()
    return render(request, "video_stream/new_invitation_form.html", {'app_name': APP_NAME, 'form': form, 'app_name': APP_NAME})


def signup(request):
    print("SIGNUP VIEW")
    if request.user.is_authenticated:
        print("SIGNUP VIEW : User is authenticated")
        return redirect('video_stream_home')
    else:
        print("SIGNUP VIEW : User is not authenticated")
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('video_stream_home')
        else:
            form = UserCreationForm()
        return render(request, 'video_stream/signup.html', {'form': form})


@login_required
def test(request):
    return render(request, "video_stream/test.html")
