from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required
from .models import Article, Category, Comment
from .forms import CommentForm


# 7. Головна сторінка: список із трьох останніх опублікованих статей [cite: 204]
def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    return render(request, 'blog/home.html', {'articles': latest_articles})


# 8. Сторінка для списку всіх опублікованих статей
def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'blog/article_list.html', {'articles': articles})


# 9. Сторінка детального опису статті та коментарів
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments})


# 10. Сторінка для списку категорій
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


# 11. Додавання коментаря
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            if request.user.is_authenticated:
                comment.user = request.user
                comment.author_name = request.user.username # Беремо ім'я з профіля
            comment.save()
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm(user=request.user)

    return render(request, 'blog/article_detail.html', {
        'article': article, 'comments': comments, 'form': form
    })


# 12. Редагування коментаря
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Перевірка прав: тільки автор може редагувати
    if comment.user != request.user:
        return HttpResponseForbidden("Ви не можете редагувати чужий коментар.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=comment.article.pk)
    else:
        form = CommentForm(instance=comment, user=request.user)
    return render(request, 'blog/edit_comment.html', {'form': form})


# 13. Видалення коментаря
@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Перевірка прав: автор АБО модератор
    is_author = comment.user == request.user
    is_moderator = request.user.groups.filter(name='Moderator').exists()

    if not (is_author or is_moderator):
         return HttpResponseForbidden("Немає прав для видалення.")

    article_pk = comment.article.pk
    comment.delete()
    return redirect('article_detail', pk=article_pk)
