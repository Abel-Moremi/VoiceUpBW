from django.shortcuts import render, redirect
from .models import VoiceUpPost
from django.contrib.auth.decorators import login_required

@login_required
def feed(request):
    userids = []
    for id in request.user.voiceupprofile.follows.all():
        userids.append(id.user)

    userids.append(request.user.id)
    posts = VoiceUpPost.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'voiceUpPost/templates/feed.html', {'posts': posts})

