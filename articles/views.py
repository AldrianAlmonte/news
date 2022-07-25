from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article
from django.core.exceptions import BadRequest



class ArticleListView(ListView):
    template_name = 'articles/list.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_list"] = Article.objects.filter(
            status=kwargs.get("status")
        ).order_by("created_on").reverse()
        return context



class ArticleDetailView(DetailView):
    template_name = "articles/detail.html"
    model = Article


class ArticleCreateView(CreateView):
    template_name = 'articles/new.html'
    model = Article
    fields = [
        "title",
        "subtitle",
        "body",
        "status"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.instance == "published":
            raise BadRequest(
                "You are not authorized to publish; Please request review."
            )
        return super().form_valid(form)



class ArticleUpdateView(UpdateView):
    template_name = "articles/edit.html"
    model = Article
    fields = [
        "title",
        "subtitle",
        "body",
        "status"
    ]
    def form_valid(self, form):
        if form.instance == "published":
            raise BadRequest(
                "You are not authorized to publish; Please request review."
            )
        return super().form_valid(form)



class ArticleDeleteView(DeleteView):
    template_name = "articles/delete.html"
    model = Article
    success_url: reverse_lazy("home") # for now



class ArticleDraftListView(ListView):
    template_name = 'articles/drafts.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_draft_list"] = Article.objects.order_by("created_on").reverse()
        return context




class ArticleDraftDetailView(DetailView):
    template_name = "articles/drafts.html"
    model = Article
