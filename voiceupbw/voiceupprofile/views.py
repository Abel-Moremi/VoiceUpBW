from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from voiceupprofile.forms import SignupForm, SigninForm
from voiceUpPost.forms import VoiceUpPostForm


# Views
@login_required
def profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == 'POST':
            form = VoiceUpPostForm(data=request.POST)

            if form.is_valid():
                voiceuppost = form.save(commit=False)
                voiceuppost.user = request.user
                voiceuppost.save()

                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
        else:
            form = VoiceUpPostForm()

        return render(request, 'profile.html', {'form': form, 'user': user})
    else:
        return redirect('/')


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/' + request.user.username + '/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignupForm(data=request.POST)
                signinform = SigninForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')
            else:
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')
        else:
            signupform = SignupForm()
            signinform = SigninForm()

        return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform})


@login_required
def signout(request):
    logout(request)
    return redirect('/')


@login_required
def follows(request, username):
    user = User.objects.get(username=username)
    profiles = user.voiceupprofile.follows.all()

    return render(request, 'users.html', {'title': 'Follows', 'profiles': profiles})


@login_required
def followers(request, username):
    user = User.objects.get(username=username)
    profiles = user.voiceupprofile.followed_by.all()

    return render(request, 'users.html', {'title': 'Followers', 'profiles': profiles})


@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    request.user.voiceupprofile.follows.add(user.voiceupprofile)

    return redirect('/' + user.username + '/')


@login_required
def stopfollow(request, username):
    user = User.objects.get(username=username)
    request.user.voiceupprofile.follows.remove(user.voiceupprofile)

    return redirect('/' + user.username + '/')