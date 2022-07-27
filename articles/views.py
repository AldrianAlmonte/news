
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article, Section, Status
from django.core.exceptions import BadRequest, PermissionDenied


class ArticlceNavbarHelper:

    def __init__(self, context):
        self.set_sections(context)
        self.set_statuses(context)

    def set_sections(self, context):
        context["sections"] = Section.objects.all()

    def set_statuses(self, context,):
        context["statuses"] = Status.objects.all()


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'articles/list.html'
    model = Article

    def get_article_list_context(self, context, section, status):
        context["article_list"] = Article.objects.filter(
                section=section
            ).filter(
                status=status
            ).order_by("created_on").reverse()
        return context




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = Status.objects.get(id=self.kwargs.get("status"))
        section = Section.objects.get(id=self.kwargs.get("section"))

        ArticlceNavbarHelper(context)

        if status.id == 1:
            return self.get_article_list_context(context, section, status)
        if self.request.user.role.id > 1:
            return self.get_article_list_context(context, section, status)
        raise PermissionDenied('Sorry! you do not have access!')



class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "articles/detail.html"
    model = Article

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if context ["article"].published == True:
    #         return context
    #     else:
    #         self.template_name = "errors/404.html"
    #         return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'articles/new.html'
    model = Article
    fields = [
        "title",
        "subtitle",
        "section",
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



class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "articles/delete.html"
    model = Article
    success_url: reverse_lazy('home')



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

