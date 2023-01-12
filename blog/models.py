from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name="blogs")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog")


class Tag(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    blog = models.ManyToManyField(Blog, related_name="tags")
