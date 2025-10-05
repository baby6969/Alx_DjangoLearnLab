# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "avatar")

class PostForm(forms.ModelForm):
# a simple comma-separated tags input
    tags = forms.CharField(required=False, help_text='Comma-separated tags',
    widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2'}))


class Meta:
    model = Post
    fields = ['title', 'content', 'tags']


def __init__(self, *args, **kwargs):
    # if instance provided, populate tags initial value
    super().__init__(*args, **kwargs)
    if self.instance and self.instance.pk:
    self.fields['tags'].initial = ', '.join([t.name for t in self.instance.tags.all()])


def clean_title(self):
 title = self.cleaned_data.get('title', '')
 if len(title) < 3:
    raise forms.ValidationError('Title must be at least 3 characters long')
 return title


def clean_tags(self):
    raw = self.cleaned_data.get('tags', '')
# return list of unique trimmed tag names
    tags = [t.strip() for t in raw.split(',') if t.strip()]
    return list(dict.fromkeys(tags))


def save(self, commit=True):
    tags = self.cleaned_data.pop('tags', [])
    post = super().save(commit=commit)
# attach tags
    if commit:
        post.tags.clear()
    for name in tags:
        tag_obj, _ = Tag.objects.get_or_create(name=name)
        post.tags.add(tag_obj)
    else:
# if not commit, ensure tags will be handled later (caller must handle)
        self._pending_tags = tags
    return post

def clean_title(self):
 title = self.cleaned_data.get('title')
 if len(title) < 3:
    raise forms.ValidationError('Title must be at least 3 characters long')
 return title


class CommentForm(forms.ModelForm):
 class Meta:
    model = Comment
    fields = ['content']
    widgets = {
    'content': forms.Textarea(attrs={'placeholder': 'Write a comment...', 'class': 'form-control', 'rows': 4}),
    }


def clean_content(self):
    content = self.cleaned_data.get('content', '').strip()
    if not content:
        raise forms.ValidationError('Comment cannot be empty')
    if len(content) > 2000:
        raise forms.ValidationError('Comment too long (2000 characters max)')
    return content