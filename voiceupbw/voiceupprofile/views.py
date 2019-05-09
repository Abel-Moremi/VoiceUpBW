from django.shortcuts import render

# Create your views here.

# Import django and models

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from voiceupprofile.forms import SignupForm, SigninForm
from voiceUpPost.forms import VoiceUpPostForm


# Views

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

                if signupform.is_valid():
                    login(request, signupform.get_user())
                    return redirect('/')
        else:
            signupform = SignupForm()
            signinform = SigninForm()

        return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform})


def signout(request):
    logout(request)
    return redirect('/')


def profiles(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})
