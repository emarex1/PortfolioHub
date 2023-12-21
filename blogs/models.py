from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    my_title = models.CharField(max_length=50)
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


class RecentPosts(models.Model):
    class Meta:
        ordering = ['-date']
    title = models.CharField(max_length=50)
    title_type = models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("recent_post_detail", kwargs={"pk": self.pk})