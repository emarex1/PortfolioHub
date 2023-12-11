from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    title = models.CharField(max_length=50)
    bio = models.CharField(max_length=300)
    resume = models.FileField(upload_to='resumes', blank=True)
    pics = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title

    def get_resume_url(self):
        if self.resume:
            return self.resume.url
        return None

    def get_profile_pic_url(self):
        if self.pics:
            return self.pics.url
        return None