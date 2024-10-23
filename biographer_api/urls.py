from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from dj_rest_auth.views import PasswordResetConfirmView
from core_apps.users.views import CustomUserDetailsView

schema_view = get_schema_view(
    openapi.Info(
        title="Biographer Haven API",
        default_version="v1",
        description="API endpoints for Biographer API Learning",
        contact=openapi.Contact(email="armanhossain.tech@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/user", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/registration", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/password/reset/confird/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
]

admin.site.site_header = "Biographer Haven API Admin"

admin.site.site_title = "Biographer Haven API Admin Portal"

admin.site.index_title = "Welcome to Biographer Haven API Portal"
