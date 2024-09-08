from helper.models.base_model import BaseModel
from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()

class Note(BaseModel):
    note_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.user.username
        
    
