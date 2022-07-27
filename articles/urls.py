from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleDraftDetailView,
    ArticleDraftListView,
    ArticleUpdateView,
    ArticleListView,
    ArticleDeleteView,
    ArticleCreateView
    
)

urlpatterns = [
    path('', ArticleListView.as_view(), {"section": 1, "status": 1}, name='home'),
    path('<int:section>/<int:status>/', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/draft/', ArticleDraftDetailView.as_view(), name='article_draft_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),

]
