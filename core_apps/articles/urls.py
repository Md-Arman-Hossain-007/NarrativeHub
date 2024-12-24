from django.urls import path

from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, ClapArticleAPIView

urlpatterns = [
    path("", ArticleListCreateAPIView.as_view(), name="article-list-create"),
    path("<uuid:id>/", ArticleRetrieveUpdateDestroyAPIView.as_view(), name="article-retrieve-update-destroy"),
    path("<uuid:article_id>/clap/", ClapArticleAPIView.as_view(), name="clap-article"),
]