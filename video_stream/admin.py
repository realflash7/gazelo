from django.contrib import admin

from .models import Video, WatchHistory, WatchingRecord


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("content", "name", "description")
    list_editable = ("name",)    # extra comma as this expects a tuple, it will be considered string else


admin.site.register(WatchHistory)
admin.site.register(WatchingRecord)