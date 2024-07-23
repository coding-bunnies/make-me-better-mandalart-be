from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.auth.models import Account


class AuthRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True, allow_blank=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and Account.objects.filter(email__iexact=email):
            raise serializers.ValidationError(
                _("A user is already registered with this e-mail address."),
            )
        return email
