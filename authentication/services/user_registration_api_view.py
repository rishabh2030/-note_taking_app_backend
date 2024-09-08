from rest_framework import generics, status, serializers
from rest_framework.response import Response
from ..serializers.user_registration_serializer import UserRegistrationSerializer
from helper.utils.values.response_values import SUCCESS,ERROR
from helper.utils.messages.user_registerions_messages import REGISTERIONS_SUCESS,INTERNAL_SERVER_ERROR,BAD_REQUEST
from helper.utils.handling.response_handling import ResponseHandling
class UserRegistrationApiView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """
        Overwrites the default create method of the CreateAPIView to handle the exception
        and return a custom JSON response.

        :param request: The request object containing the data to be saved.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: A JSON response containing the newly created object or an error message.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(ResponseHandling.success_response_message(SUCCESS,REGISTERIONS_SUCESS,serializer.data), status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
                error_details = e.detail 
                return Response(ResponseHandling.failure_response_message(ERROR,BAD_REQUEST,error_details),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR,INTERNAL_SERVER_ERROR,str(e)),status=status.HTTP_500_INTERNAL_SERVER_ERROR)