from django.contrib import admin

from .models import User, Video, View, Like, Comment, Following

admin.site.register(User)
admin.site.register(Video)
admin.site.register(View)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Following)

