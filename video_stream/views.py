from django.shortcuts import render

from outset.models import Video

def home(request):
    user_videos = Video.objects.videos_added_by_user(
        user=request.user
    )
    all_videos = Video.objects.viewable_videos(
        user=request.user
    )
    print("NEW REQUEST by : ", request.user)
    return render(request, "video_stream/home.html",
            {'nvideos': Video.objects.count(), 'my_videos': user_videos, 'all_videos': all_videos})