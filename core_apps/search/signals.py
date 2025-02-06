from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry
from core_apps.articles.models import Article

@receiver(post_save, sender=Article)
def update_article_document(sender, instance=None, created=False, **kwargs):
    if kwargs.get('created', False):
        instance.save()