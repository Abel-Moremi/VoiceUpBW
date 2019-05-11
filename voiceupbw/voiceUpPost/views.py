from django.shortcuts import render, redirect
from .models import VoiceUpPost, Comment
from django.contrib.auth.decorators import login_required


@login_required
def feed(request, username):
    userids = []
    for id in request.user.voiceupprofile.follows.all():
        userids.append(id.user)

    userids.append(request.user.id)
    posts = VoiceUpPost.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'voiceUpPost/templates/feed.html', {'posts': posts})


def post_detail(request, username, id):
    post = VoiceUpPost.objects.get(id=id)
    comments = Comment.objects.get(post=id)
    return render(request, 'post_detail.html', {'comments': comments, 'post': post})
