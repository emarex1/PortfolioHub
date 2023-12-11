from django.views.generic import ListView
from .models import UserProfile


class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'home.html'
    