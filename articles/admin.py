from django.contrib import admin
from .models import Article

admin.site.register(Article)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})
