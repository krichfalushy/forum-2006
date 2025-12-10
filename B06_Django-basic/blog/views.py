from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# 7. Головна сторінка: список із трьох останніх опублікованих статей [cite: 204]
def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    return render(request, 'blog/home.html', {'articles': latest_articles})


# 8. Сторінка для списку всіх опублікованих статей [cite: 204]
def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'blog/article_list.html', {'articles': articles})


# 9. Сторінка детального опису статті та коментарів [cite: 205]
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments})


# 10. Сторінка для списку категорій [cite: 205]
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})