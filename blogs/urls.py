from django.urls import path
from .views import HomeView#, RecentPostsLimitedView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('', RecentPostsLimitedView.as_view(), name='home'),
]