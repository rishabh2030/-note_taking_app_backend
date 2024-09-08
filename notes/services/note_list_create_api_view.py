from ..models import Note
from rest_framework import generics,status,serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from helper.utils.handling.response_handling import ResponseHandling
from ..serializers.note_serializer import NoteSerializer
from helper.utils.messages.user_registerions_messages import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOTE_ADDED_SUCESS, LIST_OF_NOTE,NOTE_DELETED_SUCESS
from helper.utils.values.response_values import ERROR,SUCCESS
from helper.utils.functions.pagination import CustomPagination

class NoteCreateApiView(generics.CreateAPIView):
    queryset = NoteSerializer.Meta.model.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Creates a new note with given data.

        :param request: The request object containing the note data.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: A JSON response containing the newly created note or an error message.
        """
        try:
            serializer = NoteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(ResponseHandling.success_response_message(SUCCESS,NOTE_ADDED_SUCESS,serializer.data), status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            error_details = e.detail
            return Response(ResponseHandling.failure_response_message(ERROR, BAD_REQUEST, error_details),status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR, INTERNAL_SERVER_ERROR, str(e)),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NoteListApiView(generics.ListAPIView):
    queryset = NoteSerializer.Meta.model.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        """
        Gets a list of notes associated with the user.

        :param request: The request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: A JSON response containing the list of notes.
        """
        try:
            user = request.user
            notes_instance_list = Note.objects.filter(user=user)
            paginator = CustomPagination()
            paginated_notes = paginator.paginate_queryset(notes_instance_list, request)
            serializer = NoteSerializer(paginated_notes, many=True)
            if not serializer.data:
                return Response({"message": "No notes found."}, status=status.HTTP_204_NO_CONTENT)
            return Response(ResponseHandling.success_response_message(SUCCESS,LIST_OF_NOTE,paginator.get_paginated_response(serializer.data).data), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(ERROR, INTERNAL_SERVER_ERROR, str(e)),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

