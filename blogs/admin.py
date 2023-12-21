from django.contrib import admin
from .models import UserProfile, RecentPosts

admin.site.register(UserProfile)
admin.site.register(RecentPosts)