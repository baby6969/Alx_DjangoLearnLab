
# Create your views here.
# blog/views.py
from django.shortcuts import  redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render 
from  django.views import view
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
    template_name = 'blog/posts_list.html' # app/templates/blog/posts_list.html
    context_object_name = 'posts'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' # template dir
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'


def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = 'login'


def test_func(self):
    post = self.get_object()
    return post.author == self.request.user



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'


def test_func(self):
    post = self.get_object()
    return post.author == self.request.user

    Comment views
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    login_url = 'login'


def dispatch(self, request, *args, **kwargs):
    self.post = get_object_or_404(Post, pk=kwargs.get('post_pk'))
    return super().dispatch(request, *args, **kwargs)


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