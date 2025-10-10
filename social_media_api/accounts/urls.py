from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
   path('register/', registerViews.as_view(), name= 'register'),
   path('login',loginViews.as_view() ,name='login'),


]


















