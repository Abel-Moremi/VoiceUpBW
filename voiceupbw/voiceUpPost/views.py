from django.shortcuts import render
from .models import VoiceUpPost


def feed(request):
    userids = []
    for id in request.user.voiceupprofile.follows.all():
        userids.append(id.user)

    userids.append(request.user.id)
    posts = VoiceUpPost.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'feed.html', {'posts': posts})
