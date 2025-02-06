import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        OTHER = "O", _("Other")

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    phone_number = PhoneNumberField(
        verbose_name=_("phone number"), max_length=30, default="+880-1923675361"
    )
    gender = models.CharField(
        verbose_name=_("gender"),
        max_length=20,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    country = CountryField(
        verbose_name=_("country"), default="BD", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"), max_length=180, default="Dhaka", blank=False, null=False
    )
    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), default="/profile_default.png"
    )
    twitter_handle = models.CharField(
        verbose_name=_("twitter handle"), max_length=20, blank=True
    )
    followers = models.ManyToManyField(
        to="self",
        verbose_name=_("followers count"),
        symmetrical=False,
        related_name="following",
        blank=True,
    )
    about_me = models.TextField(
        verbose_name=_("about me"),
        default="say something about yourself",
    )

    def __str__(self):
        return f"{self.user.first_name}'s Profile"

    def follow(self, user_profile):
        self.followers.add(user_profile)

    def unfollow(self, user_profile):
        self.followers.remove(user_profile)

    def check_following(self, user_profile):
        return self.followers.filter(pkid=user_profile.pkid).exists()
