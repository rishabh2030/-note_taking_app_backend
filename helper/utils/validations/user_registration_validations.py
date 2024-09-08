import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from helper.utils.messages.user_registerions_messages import INVALID_USERNAME,USERNAME_ALREADY_EXISTS,EMAIL_ALREADY_EXISTS
User = get_user_model()


class  UserRegistrationValidators:
    @staticmethod
    def validate_username(value):
        if not re.match(r'^[a-z0-9._]+$', value):
            raise serializers.ValidationError(INVALID_USERNAME)
        elif User.objects.filter(username=value).exists():
            raise serializers.ValidationError(USERNAME_ALREADY_EXISTS)
        return value
    @staticmethod
    def validate_email(value):
        if value == "":
            return value
        elif User.objects.filter(email=value).exists():
            raise serializers.ValidationError(EMAIL_ALREADY_EXISTS)
        return value