from django.views.generic import ListView, DetailView
from .models import UserProfile


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'userprofile_detail.html'

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'home.html'