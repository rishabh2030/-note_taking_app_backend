from rest_framework import serializers
from users.entity.user import User
from helper.utils.validations.user_registration_validations import  UserRegistrationValidators 

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False, allow_blank=True, validators=[UserRegistrationValidators.validate_email]
    )

    username = serializers.CharField(
        required=True,
        max_length=100,
        min_length=2,
        validators=[UserRegistrationValidators.validate_username],
    )
    
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ("email","username","password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Creates a new user with the validated data and sets the password.

        Args:
            validated_data (dict): The validated data from the serializer.

        Returns:
            User: The newly created user.
        """
        user_obj = User.objects.create_user(**validated_data)
        user_obj.set_password(validated_data["password"])
        return user_obj