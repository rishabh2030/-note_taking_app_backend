from rest_framework import serializers


class LoginOtpVerificationSerializer(serializers.Serializer):
    identity = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=6)