# Import django forms and models

from django import forms
from django.utils.html import strip_tags
from .models import VoiceUpPost


class VoiceUpPostForm(forms.ModelForm):

    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))

    class Meta:
        model = VoiceUpPost
        exclude = ('user',)
