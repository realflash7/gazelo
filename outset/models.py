from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=40, blank=False)
    full_name = models.CharField(max_length=400, blank=False)
    email = models.CharField(max_length=400, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    videos_count = models.IntegerField()
    followers_count = models.IntegerField()
    following_count = models.IntegerField()

class Video(models.Model):
    name = models.CharField(max_length=400, blank=False)
    user = models.ForeignKey(User, related_name="added_by", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)
    access_level = models.IntegerField() #maybe - 0=private, 1=public, 2=masked
    url_key = models.CharField(max_length=10, blank=False)
    size = models.IntegerField()
    views_count = models.IntegerField()
    likes_count = models.IntegerField()
    comments_count = models.IntegerField()

class View(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="viewed_by", on_delete=models.CASCADE)
    last_view_date = models.DateTimeField()

class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="liked_by", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="commented_by", on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=False)
    is_top_level = models.BooleanField()    # true=comment, false=reply
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)


