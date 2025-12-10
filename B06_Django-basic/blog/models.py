from django.db import models

# Create your models here.
from django.db import models


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
    author = models.CharField(max_length=255)  # Реалізовано як рядок [cite: 201]
    text = models.TextField()
    image = models.CharField(max_length=255, help_text="Image URL")  # [cite: 169, 200]
    publication_date = models.DateField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # [cite: 182]
    tags = models.ManyToManyField(Tag) # [cite: 183]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # [cite: 197]

    def __str__(self):
        return f"Comment by {self.author}"
