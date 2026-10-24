from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True, verbose_name="Изображение") # Новое поле
    content = models.TextField(verbose_name="Текст статьи")
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)

    def __str__(self):
        return self.title
