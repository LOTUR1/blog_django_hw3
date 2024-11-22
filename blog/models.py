from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_date__lte = timezone.now())

    def by_author(self, author):
        return self.filter(author=author)

class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date = models.DateTimeField(null = True, blank = True)
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to='post_images', null=True, blank=True)

    objects = models.Manager()
    published_posts = PublishedPostManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(null = True, blank = True)