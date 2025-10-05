"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),   # 👈 Add this line
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]

urlpatterns = [
path('posts/', views.PostListView.as_view(), name='posts'),
path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]



# Serve media files in dev (for avatar)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
