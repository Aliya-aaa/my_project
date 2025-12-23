from django.urls import path
from . import views

app_name = 'articles'  # ← обязательно!

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:id>/edit/', views.article_edit, name='article_edit'),
]