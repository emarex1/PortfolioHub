from django.views.generic import ListView, DetailView, View
from .models import UserProfile, RecentPosts
from django.shortcuts import render


#class UserProfileListView(ListView):
#    model = UserProfile
#    template_name = 'home.html'
#    context_object_name = 'items'

 #   def get_queryset(self):
#        profile = UserProfile.objects.all()
#        posts = RecentPosts.objects.all()[:2]  # Display only two recent posts
#        return list(profile) + list(posts)

class HomeView(View):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {
            'profile': UserProfile.objects.all(),
            'posts': RecentPosts.objects.all()[:2],
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class RecentPostsDetailView(DetailView):
    model = RecentPosts
    template_name = 'recent_posts_detail.html'
    #context_object_name = 'post'

#class RecentPostsLimitedView(ListView):
    #model = RecentPosts
    #template_name = 'home.html'
    #context_object_name = 'posts'
    #queryset = RecentPosts.objects.all()[:2]  # Display only two posts

class RecentPostsFullView(ListView):
    model = RecentPosts
    template_name = 'recent_posts_list_full.html'
    #context_object_name = 'posts'
    queryset = RecentPosts.objects.all()  # Display all posts