from django.urls import path

from outset.views import profile

urlpatterns = [
    path('<slug:username>/',
         profile,
         name="outset_profile")
]