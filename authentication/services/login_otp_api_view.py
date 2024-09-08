from rest_framework import generics,status,serializers
from rest_framework.response import Response
from helper.utils.values.response_values import ERROR,SUCCESS
from helper.utils.functions.user_functions import UserFunctions
from ..serializers.login_serializer_otp import LoginSerializerOtp
from helper.utils.handling.response_handling import ResponseHandling
from helper.utils.messages.user_registerions_messages import NOT_FOUND_IDENTITY,OTP_SENT,BAD_REQUEST,INTERNAL_SERVER_ERROR
class LoginOtpApiView(generics.CreateAPIView):
    serializer_class = LoginSerializerOtp
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
            UserFunctions.generate_otp(user_obj)
            return Response(ResponseHandling.success_response_message(SUCCESS,OTP_SENT,None), status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            error_details = e.detail
            return Response(ResponseHandling.failure_response_message(ERROR,BAD_REQUEST,error_details),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR,INTERNAL_SERVER_ERROR,str(e)),status=status.HTTP_500_INTERNAL_SERVER_ERROR)