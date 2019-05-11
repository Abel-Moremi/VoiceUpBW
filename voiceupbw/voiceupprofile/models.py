from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class VoiceUpProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    district = models.CharField(max_length=100)
    isPolitician = models.BooleanField(default=False)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)


User.voiceupprofile = property(lambda u: VoiceUpProfile.objects.get_or_create(user=u)[0])
