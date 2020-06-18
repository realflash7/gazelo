from django.contrib import admin

from .models import Profile, Content, View, Like, Comment, Following

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ("auth_user", "followers_count")

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "access_level", "views_count", "likes_count", "comments_count")
    list_editable = ("access_level",)    # extra comma as this expects a tuple, it will be considered string else


admin.site.register(View)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Following)

