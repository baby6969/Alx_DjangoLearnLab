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

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
 class Meta:
    model = Post
    fields = ['title', 'content']
    widgets = {
    'title': forms.TextInput(attrs={'placeholder': 'Enter post title', 'class': 'form-control'}),
    'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 10}),
}


def clean_title(self):
 title = self.cleaned_data.get('title')
 if len(title) < 3:
    raise forms.ValidationError('Title must be at least 3 characters long')
 return title