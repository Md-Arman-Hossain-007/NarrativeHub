from django.urls import path

from .views import RatingCreateAPIView

urlpatterns = [
    path(
        "rate-article/<uuid:article_id>/",
        RatingCreateAPIView.as_view(),
        name="rating-create",
    ),
]
