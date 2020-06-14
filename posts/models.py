from django.db import models
from django.contrib.auth import get_user_model
# from django_extensions.db.fields import AutoSlugField
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
# import random
# import string

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

# def get_rand_string():
#     return random.sample(string.ascii_lowercase, 10)

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    # slug = AutoSlugField(populate_from='title')
    slug = models.SlugField()

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + '...'

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    # def get_default(self):
    #     return random.sample(string.ascii_lowercase, 10)
    
