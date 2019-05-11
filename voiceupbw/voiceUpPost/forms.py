# Import django forms and models

from django import forms
from .models import VoiceUpPost, Comment


class VoiceUpPostForm(forms.ModelForm):

    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))

    class Meta:
        model = VoiceUpPost
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body',)

