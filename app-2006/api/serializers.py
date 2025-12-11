from rest_framework import serializers
from blog.models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'text', 'publication_date']


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'image', 'publication_date', 'author_name', 'comments']
