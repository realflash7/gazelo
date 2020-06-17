from django.urls import path

from outset.views import profile

urlpatterns = [
    path('<str:id>',
         profile,
         name="outset_profile")
]