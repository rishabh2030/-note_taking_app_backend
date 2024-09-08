from rest_framework import serializers

class LoginSerializerOtp(serializers.Serializer):
    identity = serializers.CharField(max_length=100)