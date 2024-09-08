from rest_framework import generics,status,serializers
from ..serializers.login_otp_verfification_serializer import LoginOtpVerificationSerializer
from helper.utils.functions.user_functions import UserFunctions
from rest_framework.response import Response
from helper.utils.values.response_values import ERROR,SUCCESS
from helper.utils.handling.response_handling import ResponseHandling
from helper.utils.messages.user_registerions_messages import INTERNAL_SERVER_ERROR,LOGIN_SUCESS,NOT_FOUND_IDENTITY,INVALID_OTP,OTP_EXIPRED,BAD_REQUEST
from master.models import OTPManager
from django.utils import timezone
from django.contrib.auth import get_user_model

user = get_user_model()

class LoginOtpVerificationApiView(generics.CreateAPIView):
    serializer_class = LoginOtpVerificationSerializer
    def create(self, request, *args, **kwargs):
        """
        Overwrites the default create method of the GenericAPIView to handle the exception
        and return a custom JSON response.

        :param request: The request object containing the data to be saved.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: A JSON response containing the newly created object or an error message.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            if UserFunctions.get_user(serializer.data['identity']) is False:
                return Response(ResponseHandling.failure_response_message(ERROR,NOT_FOUND_IDENTITY,None),status=status.HTTP_404_NOT_FOUND)
            user_obj = UserFunctions.get_user(serializer.data['identity'])
            
            if OTPManager.objects.filter(user=user_obj,otp=serializer.data['otp'],is_used=False).exists():
                otp_instance = OTPManager.objects.filter(user=user_obj,otp=serializer.data['otp']).last()
                otp_instance.is_used = True
                otp_instance.save()
                if timezone.now() > otp_instance.expired_at:
                    return Response(ResponseHandling.failure_response_message(ERROR,OTP_EXIPRED,None),status=status.HTTP_404_NOT_FOUND)
                token, refresh_token = user_obj.get_tokens()
                token = {"access_token": token,"refresh_token": refresh_token}    
                return Response(ResponseHandling.success_response_message(SUCCESS,LOGIN_SUCESS,token), status=status.HTTP_200_OK)
        
            return Response(ResponseHandling.failure_response_message(ERROR,INVALID_OTP,None),status=status.HTTP_404_NOT_FOUND)
        except serializers.ValidationError as e:
                error_details = e.detail
                return Response(ResponseHandling.failure_response_message(ERROR,BAD_REQUEST,error_details),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR,INTERNAL_SERVER_ERROR,str(e)),status=status.HTTP_500_INTERNAL_SERVER_ERROR)        