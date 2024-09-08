from rest_framework import serializers
from ..models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('note_uuid','title','content')
    
    def create(self, validated_data):
        note_instance = Note.objects.create(**validated_data)
        return note_instance