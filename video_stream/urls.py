from django.urls import path

from .views import home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='video_stream_home'),
    path('login/',
         LoginView.as_view(template_name="video_stream/login_form.html"),
         name="video_stream_login"),
    path('logout/',
         LogoutView.as_view(),
         name="video_stream_logout")
]