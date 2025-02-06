from django.urls import path

from core_apps.responses.views import (
    ResponseListCreateApiView,
    ResponseUpdateDestroyApiView,
)

urlpatterns = [
    path(
        "article/<uuid:article_id>/",
        ResponseListCreateApiView.as_view(),
        name="article_responses",
    ),
    path("<uuid:id>/", ResponseUpdateDestroyApiView.as_view(), name="response_detail"),
]
