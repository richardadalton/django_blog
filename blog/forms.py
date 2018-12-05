from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['published_date', 'author', 'views']
        widgets = {
            'tags': forms.TextInput(attrs={'data-role': 'tagsinput'}),
        }