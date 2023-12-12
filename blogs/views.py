from django.views.generic import ListView, DetailView
from .models import UserProfile


class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'home.html'

class RecentPostsDetailView(DetailView):
    model = RecentPosts
    template_name = 'recent_posts_detail.html'
    context_object_name = 'post'

class RecentPostsLimitedView(ListView):
    model = RecentPosts
    template_name = 'recent_posts_list_limited.html'
    context_object_name = 'posts'
    queryset = RecentPosts.objects.all()[:2]  # Display only two posts

class RecentPostsFullView(ListView):
    model = RecentPosts
    template_name = 'recent_posts_list_full.html'
    context_object_name = 'posts'
    queryset = RecentPosts.objects.all()  # Display all posts