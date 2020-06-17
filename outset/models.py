from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver

from gazelo.settings import DEFAULT_USER_BIO

CONTENT_ACCESS_LEVEL = (
    (0, "Private, nobody can view"),
    (1, "Only followers can view"),
    (2, "Public, anybody can view")
)


class ContentQuerySet(models.QuerySet):
    def contents_added_by_user(self, user):
        return self.filter(
            user=user
        )
    def viewable_contents(self, user):
        return self.filter(
            # TODO: for masked access level
            Q(access_level=2) | Q(user=user)
        )


class UserDetail(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    bio = models.CharField(max_length=800, default=DEFAULT_USER_BIO)
    auth_user = models.OneToOneField(User, related_name="user_detail", on_delete=models.CASCADE, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('outset_profile', args=[self.auth_user.username])

    def __str__(self):
        return "{0}".format(
            self.auth_user.username)


class Content(models.Model):
    user = models.ForeignKey(User, related_name="created_contents", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    access_level = models.IntegerField(default=0, choices=CONTENT_ACCESS_LEVEL) #maybe - 0=private, 1=masked, 2=public
    views_count = models.IntegerField()
    likes_count = models.IntegerField()
    comments_count = models.IntegerField()
    allow_comments = models.BooleanField(default=False)

    objects = ContentQuerySet.as_manager()

    def __str__(self):
        return "{0}".format(
            self.id)

class View(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="views_by_user", on_delete=models.CASCADE)
    last_view_date = models.DateTimeField()

    def __str__(self):
        return "{0} viewed {1}".format(
            self.user, self.content)


class Like(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="likes_by_user", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} liked {1}".format(
            self.user, self.content)


class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments_by_user", on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=False)
    is_top_level = models.BooleanField()    # true=comment, false=reply
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{1} commented \"{1}\" on {2}".format(
            self.user, self.text, self.content)


class Following(models.Model):
    user = models.ForeignKey(User, related_name="user_followers", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="user_following", on_delete=models.CASCADE)

    def __str__(self):
        return "{0} follows {1}".format(
            self.follower, self.user)


