from rest_framework import serializers

class LoginSerializerPassword(serializers.Serializer):
    identity = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)