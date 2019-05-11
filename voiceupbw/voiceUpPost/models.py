from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class VoiceUpPost(models.Model):
    user = models.ForeignKey(User, related_name='voiceuppost', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    post = models.ForeignKey(VoiceUpPost, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __Str__(self):
        return self.user
