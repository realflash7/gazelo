from django.db import models

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