from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from phonenumber_field.modelfields import PhoneNumberField

from gazelo.settings import INVITATION_MESSAGE
from outset.models import Content


class Video(models.Model):
    name = models.CharField(max_length=400, blank=False)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(max_length=40000, null=True, blank=True, default="")
    data_source = models.CharField(max_length=400, blank=True, default="NONE" , null=False)
    slug = models.SlugField()
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


class Invitation(models.Model):
    from_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="invitations_sent")
    to_user_email = models.EmailField(
        verbose_name="Friend's email",
        help_text="Please add the email of your friend you want to invite."
    )
    to_user_phone_no = PhoneNumberField(
        blank=True,
        verbose_name="Friend's contact number",
        help_text="Please add the contact number of your friend you want to invite."
    )
    message = models.CharField(default=INVITATION_MESSAGE, max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "invitation from {0} to email={1},phone={2}".format(
            self.from_user, self.to_user_email, self.to_user_phone_no
        )


#    def clean(self):
 #      if self.to_user_email is None and self.to_user_phone_no is None:
  #          raise ValidationError("Email and Phone both cannot be empty")



