from django.urls import path
from .views import UserProfileListView, UserProfileDetailView

urlpatterns = [
    path('userprofile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile_detail'),
    path('', UserProfileListView.as_view(), name='home'),
]