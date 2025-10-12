from django.urls import path
from .views import RegisterView, LoginView 
from .views import FollowUserView, UnfollowUserView, FollowingListView, FollowersListView


urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view(), name='login'),
   path('profile/', ProfileView.as_view(), name='profile'),
   path('follow/', FollowUserView.as_view(), name='follow'),
   path('unfollow/', UnfollowUserView.as_view(), name='unfollow'),
   path('following/', FollowingListView.as_view(), name='following-list'),
   path('followers/', FollowersListView.as_view(), name='followers-list'),
   path('api/accounts/', include('accounts.urls')),
   path('api/', include('posts.urls')),

]





















