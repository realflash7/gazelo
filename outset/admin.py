from django.contrib import admin

from .models import UserDetails, Video, View, Like, Comment, Following

@admin.register(UserDetails)
class UserAdmin(admin.ModelAdmin):
    list_display = ("auth_user", "videos_count", "followers_count")

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "access_level", "views_count", "likes_count", "comments_count")
    list_editable = ("access_level",)    # extra comma as this expects a tuple, it will be considered string else

admin.site.register(View)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Following)

