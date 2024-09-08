from rest_framework import generics,serializers,status
from rest_framework.response import Response
from ..serializers.note_serializer import NoteSerializer
from ..models import Note
from helper.utils.handling.response_handling import ResponseHandling
from rest_framework.permissions import IsAuthenticated
from helper.utils.messages.user_registerions_messages import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOTE_UPDATED_SUCESS, GOT_THE_NOTE,NOT_FOUND_NOTE, NOTE_DELETED_SUCESS
from helper.utils.values.response_values import ERROR,SUCCESS
class NoteEditDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'note_uuid'
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        """
        Get a note by given note_uuid.

        Args:
            request: The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response containing the result of the operation.
        """
        try:
            note_uuid = kwargs.get(self.lookup_field)
        
            user = request.user
            note = Note.objects.filter(note_uuid=note_uuid, user=user).last()
            
            if note is None:
                return Response(ResponseHandling.failure_response_message(ERROR, BAD_REQUEST, NOT_FOUND_NOTE),status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(note)
            
            return Response(ResponseHandling.success_response_message(SUCCESS, GOT_THE_NOTE, serializer.data),status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR, INTERNAL_SERVER_ERROR, str(e)),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def patch(self, request, *args, **kwargs):
        """
        Partially updates a note by given note_uuid.

        Args:
            request: The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response containing the result of the operation.
        """
        try:
            note_uuid = kwargs.get('note_uuid')
            user = request.user
            note = Note.objects.filter(note_uuid=note_uuid,user=user).last()
            if note is None:
                return Response(ResponseHandling.failure_response_message(ERROR, BAD_REQUEST, NOT_FOUND_NOTE), status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(note,data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                serializer.save()
                return Response(ResponseHandling.success_response_message(SUCCESS,NOTE_UPDATED_SUCESS,serializer.data), status=status.HTTP_205_RESET_CONTENT)
        except serializers.ValidationError as e:
            error_details = e.detail
            return Response(ResponseHandling.failure_response_message(ERROR, BAD_REQUEST, error_details),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR, INTERNAL_SERVER_ERROR, str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR))

    def delete(self, request, *args, **kwargs):
        """
        Deletes a note by given note_uuid.
        
        Args:
            request: The request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        
        Returns:
            Response: A JSON response containing the result of the operation.
        """
        try:
            note_uuid = kwargs.get(self.lookup_field)
            user = request.user
            note = Note.objects.filter(note_uuid=note_uuid, user=user).last()
            
            if note is None:
                return Response(
                    ResponseHandling.failure_response_message(
                        ERROR, BAD_REQUEST, NOT_FOUND_NOTE
                    ),
                    status=status.HTTP_404_NOT_FOUND
                )
            
            note.delete()
            
            return Response(
                ResponseHandling.success_response_message(
                    SUCCESS, NOTE_DELETED_SUCESS,None
                ),
                status=status.HTTP_204_NO_CONTENT
            )
        
        except Exception as e:
            return Response(
                ResponseHandling.failure_response_message(
                    ERROR, INTERNAL_SERVER_ERROR, str(e)
                ),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )