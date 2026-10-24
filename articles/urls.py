from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView # Добавили LoginView
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('like/<int:pk>/', views.like_article, name='like_article'),
    path('profile/', views.profile, name='profile'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('register/', views.register, name='register'),
    # Указываем путь к нашему HTML-шаблону
    path('login/', LoginView.as_view(template_name='articles/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='article_list'), name='logout'),
]
