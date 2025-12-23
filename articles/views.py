from django.shortcuts import render, redirect, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('articles:article_list')
    return render(request, 'articles/form.html', {'title': 'Создать статью'})


def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:article_list')
    return render(request, 'articles/form.html', {
        'title': 'Редактировать статью',
        'article': article
    })
