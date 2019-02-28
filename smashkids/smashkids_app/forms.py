from django import forms
from smashkids_app.models import *

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("author", "title", "text")

        widget = {
            "title":forms.TextInput(attrs={"class":"textinputclass"}),
            "text":forms.Textarea(attrs={"class":"editable medium-editor-text-area postcontent"})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", "text")
        widgets = {
            "author":forms.TextInput(attrs={"class": "textinputclass"}),
            "text":forms.Textarea(attrs={"class":"editable medium-editor-text-area"})
        }
