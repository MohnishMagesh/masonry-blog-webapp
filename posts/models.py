from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    # CATEGORIES = [
    #     (TECHNOLOGY,'Technology'),
    #     (HISTORY,'History'),
    #     (PROGRAMMING,'Programming'),
    #     (BUSINESS,'Business'),
    #     (WORK,'Work')
    # ]
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + '...'
