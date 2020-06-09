from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

VIDEO_ACCESS_LEVEL = (
    (0, "Private, nobody can view"),
    (1, "Only followers can view"),
    (2, "Public, anybody can view")
)

class VideoQuerySet(models.QuerySet):
    def videos_added_by_user(self, user):
        return self.filter(
            user=user
        )
    def viewable_videos(self, user):
        return self.filter(
            # TODO: for masked access level
            Q(access_level=2) | Q(user=user)
        )


class UserDetails(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    bio = models.CharField(max_length=800, default="")
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    videos_count = models.IntegerField()
    followers_count = models.IntegerField()
    following_count = models.IntegerField()

    def __str__(self):
        return "{0}".format(
            self.auth_user.username)

class Video(models.Model):
    name = models.CharField(max_length=400, blank=False)
    user = models.ForeignKey(User, related_name="added_by", on_delete=models.CASCADE)
    description = models.TextField(max_length=40000, null=True, blank=True, default="")
    data_source = models.CharField(max_length=400, blank=True, default="NONE" , null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    access_level = models.IntegerField(default=0, choices=VIDEO_ACCESS_LEVEL) #maybe - 0=private, 1=public, 2=masked
    url_key = models.CharField(max_length=10, blank=False)
    size = models.IntegerField()
    views_count = models.IntegerField()
    likes_count = models.IntegerField()
    comments_count = models.IntegerField()
    allow_comments = models.BooleanField(default=False)

    objects = VideoQuerySet.as_manager()

    def __str__(self):
        return "{0}".format(
            self.name)

class View(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="viewed_by", on_delete=models.CASCADE)
    last_view_date = models.DateTimeField()

    def __str__(self):
        return "{0} viewed {1}".format(
            self.user, self.video)

class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="liked_by", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} liked {1}".format(
            self.user, self.video)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="commented_by", on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=False)
    is_top_level = models.BooleanField()    # true=comment, false=reply
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{1} commented \"{1}\" on {2}".format(
            self.user, self.text, self.video)

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)

    def __str__(self):
        return "{0} follows {1}".format(
            self.follower, self.user)


