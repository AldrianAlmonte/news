from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleDraftDetailView,
    ArticleDraftListView,
    ArticleUpdateView,
    ArticleListView,
    ArticleDeleteView,
    
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/draft/', ArticleDraftDetailView.as_view(), name='article_draft_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleDeleteView.as_view(), name='article_new'),

]
