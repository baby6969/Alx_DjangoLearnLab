
# Create your views here.
# blog/views.py
from calendar import c
from django.shortcuts import  redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render 
from  django.views import view
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm

def home_view(request):
    return render(request, 'blog/base.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 10

def form_valid(self, form):
    form.instance.author = self.request.user
    form.instance.post = self.post
    return super().form_valid(form)


def get_success_url(self):
    return reverse('post-detail', kwargs={'pk': self.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    login_url = 'login'


def test_func(self):
    comment = self.get_object()
    return comment.author == self.request.user


def get_success_url(self):
    return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    login_url = 'login'


def test_func(self):
    comment = self.get_object()
    return comment.author == self.request.user


def get_success_url(self):
    return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})


# Tag list (posts for a tag)
class TagListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html' # reuse list template
    context_object_name = 'posts'
    paginate_by = 10


def get_queryset(self):
    tag_name = self.kwargs.get('tag_name')
    return Post.objects.filter(tags__name__iexact=tag_name).distinct()


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tag_name'] = self.kwargs.get('tag_name')
    return context


# Search view
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10


def get_queryset(self):
 q = self.request.GET.get('q', '').strip()
 if not q:
     return Post.objects.none()


# search by title, content, or tag name (case-insensitive)
 return Post.objects.filter(
    Q(title__icontains=q) |
    Q(content__icontains=q) |
    Q(tags__name__icontains=q)
    ).distinct()


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['query'] = self.request.GET.get('q', '')
    return context