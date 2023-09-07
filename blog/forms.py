from django import forms
from .models import Post , Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'content ': SummernoteWidget(),
            'content': SummernoteInplaceWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Comment']
