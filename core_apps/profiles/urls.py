from django.urls import path

from .views import (
    FollowAPIView,
    FollowerListAPIView,
    FollowingListAPIView,
    ProfileDetailAPIView,
    ProfileListAPIView,
    UnfollowAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", ProfileDetailAPIView.as_view(), name="me-profile"),
    path("me/update/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path("me/follower/", FollowerListAPIView.as_view(), name="followers"),
    path("me/following/", FollowingListAPIView.as_view(), name="following"),
    path("<uuid:user_id>/follow/", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowAPIView.as_view(), name="unfollow"),
]
