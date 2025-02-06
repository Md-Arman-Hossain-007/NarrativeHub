from django.db import models
from django.contrib.auth import get_user_model
from core_apps.articles.models import Article
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Rating(TimeStampedModel):
    RATING_CHOICES = [
        (1, "Poor"),
        (2, "Fair"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent"),
    ]
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="ratings"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    review = models.TextField(blank=True)

    class Meta:
        unique_together = ("user", "article")
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return f"{self.user.first_name} rated {self.article.title} as {self.get_rating_display()}"
