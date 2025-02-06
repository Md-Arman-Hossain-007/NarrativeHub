from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from core_apps.articles.models import Article
from core_apps.responses.models import Response
from core_apps.responses.serializers import ResponseSerializer


class ResponseListCreateApiView(generics.ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        article_id = self.kwargs.get("article_id")
        return Response.objects.filter(article__id=article_id, parent_response=None)

    def perform_create(self, serializer):
        user = self.request.user
        article_id = self.kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)
        serializer.save(user=user, article=article)


class ResponseUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def perform_update(self, serializer):
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied("You do not have permission to edit this response.")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied(
                "You do not have permission to delete this response."
            )
        instance.delete()
