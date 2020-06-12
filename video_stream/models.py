from django.db import models
from django.contrib.auth.models import User

from outset.models import Content


class Video(models.Model):
    name = models.CharField(max_length=400, blank=False)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(max_length=40000, null=True, blank=True, default="")
    data_source = models.CharField(max_length=400, blank=True, default="NONE" , null=False)
    url_key = models.CharField(max_length=10, blank=False)
    size = models.IntegerField()

    def __str__(self):
        return "{0}".format(
            self.name)


class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    latest_position = models.DurationField()

    def __str__(self):
        return "{0} watched {1}".format(
            self.user, self.video)


class WatchingRecord(models.Model):
    watch_history = models.OneToOneField(WatchHistory, on_delete=models.CASCADE, primary_key=True)
    last_modified_timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()

    def __str__(self):
        return "{0}".format(
            self.watch_history)


