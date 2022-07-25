from django.contrib import admin
from .models import (
    Section,
    ArticleType,
    Article
)


admin.site.register(
    [
        Section,
        ArticleType,
        Article
    ])