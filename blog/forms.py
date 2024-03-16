from django import forms
from .models import BlogPost
from django.contrib.auth.models import User
from froala_editor.widgets import FroalaEditor

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories', 'tags', 'image']
        widgets = {
            'content': FroalaEditor(options={'toolbarInline': False, 'height': 400, 'theme': 'dark'}),
        }
