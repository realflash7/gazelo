from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from outset.models import Content

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
            {'ncontents': Content.objects.count(), 'my_contents': user_contents, 'all_contents': all_contents})