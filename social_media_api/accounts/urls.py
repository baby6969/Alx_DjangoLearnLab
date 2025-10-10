from django.urls import path
from views import RegisterView, LoginView, ProfileView

urlpatterns = [
   path('register/', registerview.as_view(), name= 'register'),
   path('login',loginview.as_view() ,name='login'),


]


















