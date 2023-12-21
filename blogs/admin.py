from django.contrib import admin
from .models import UserProfile, RecentPosts, FeaturedPosts

admin.site.register(UserProfile)
admin.site.register(RecentPosts)
admin.site.register(FeaturedPosts)