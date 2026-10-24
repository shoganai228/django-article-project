from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

@login_required
@login_required
def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    # Если запрос отправлен через HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'articles/includes/like_button.html', {'article': article, 'user': request.user})

    return redirect(request.META.get('HTTP_REFERER', 'article_list'))

@login_required
def profile(request):
    liked_articles = request.user.liked_articles.all()
    return render(request, 'articles/profile.html', {'liked_articles': liked_articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

# Новая функция регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Сразу авторизуем пользователя после создания аккаунта
            return redirect('article_list')
    else:
        form = UserCreationForm()
    return render(request, 'articles/register.html', {'form': form})
