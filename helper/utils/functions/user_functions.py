from django.contrib.auth import get_user_model
from master.models import OTPManager
from django.db.models import Q
import random
User = get_user_model()


class UserFunctions:
    @staticmethod
    def get_user(user):
        """
        Given a username or email, this function will return the corresponding
        User model instance if it exists, otherwise it will return False.

        :param user: The username or email to search for.
        :return: The User model instance for the given user, or False if no
                 such user exists.
        """
        if User.objects.filter(Q(email=user) | Q(username=user)).last():
            user_obj = User.objects.filter(Q(email=user) | Q(username=user)).last()
            return user_obj
        else:
            return False
    @staticmethod
    def generate_otp(user):
        otp = random.randint(100000, 999999)
        otp_obj = OTPManager.objects.create(user=user,otp=otp)
        otp_obj.save()
        return 