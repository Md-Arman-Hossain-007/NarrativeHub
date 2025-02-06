from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ArticleDocument
from .serializers import ArticleElasticSearchSerializer

class ArticleElasticSearchViewSet(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleElasticSearchSerializer
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend
    ]
    search_fields = (
        "title",
        "description",
        "body",
        "author_first_name",
        "author_last_name",
        "tags",
    )
    filter_fields = {
        "slug": "slug.raw",
        "tags": "tags",
        "created_at": "created_at"
    }
    ordering_fields = {
        "created_at": "created_at"
    }
    ordering = ("-created_at",)