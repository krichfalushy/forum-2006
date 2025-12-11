from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from blog.models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_published=True).order_by('-publication_date')
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
