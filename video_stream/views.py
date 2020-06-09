from django.shortcuts import render

from outset.models import Video

def home(request):
    my_videos = Video.objects.videos_added_by_user(request.user)
    all_videos = Video.objects.viewable_videos(request.user)
    return render(request, "video_stream/home.html",
            {'nvideos': Video.objects.count()},
            {'my_videos': my_videos},
            {'all_videos': all_videos})