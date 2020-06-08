from django.contrib import admin

from .models import User, Video, View, Like, Comment, Following

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "is_active", "videos_count", "followers_count")
    list_editable = ("is_active",)    # extra comma as this expects a tuple, it will be considered string else

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "access_level", "views_count", "likes_count", "comments_count")
    list_editable = ("access_level",)
    
admin.site.register(View)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Following)

