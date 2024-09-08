from django.contrib import admin
from django.urls import path,include
from .services.note_list_create_api_view import NoteCreateApiView,NoteListApiView
from .services.note_editi_delete_api_view import NoteEditDeleteApiView
urlpatterns = [
    path("note-create/",NoteCreateApiView.as_view(),name="note-create-api-view"),
    path("note-list/",NoteListApiView.as_view(),name="note-list-api-view"),
    path("get-note/<str:note_uuid>/",NoteEditDeleteApiView.as_view(),name="get-note-api-view"),
    path("update-note/<str:note_uuid>/",NoteEditDeleteApiView.as_view(),name="update-note-api-view"),
    path("delete-note/<str:note_uuid>/",NoteEditDeleteApiView.as_view(),name="delete-note-api-view"),

]