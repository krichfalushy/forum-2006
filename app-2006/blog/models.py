from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Fontawesome icon code")  # [cite: 174, 199]
    image = models.CharField(max_length=255, help_text="Image URL")  # [cite: 175, 200]

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    author_name = models.CharField(max_length=255, default="Anonymous")

    image = models.CharField(max_length=255, help_text="Image URL")
    publication_date = models.DateField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # [cite: 197]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    author_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Comment by {self.author}"
