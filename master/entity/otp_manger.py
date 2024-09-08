from helper.models.base_model import BaseModel
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models

user = get_user_model()

class OTPManager(BaseModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)
    expired_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expired_at:
            self.expired_at = timezone.now() + timezone.timedelta(hours=24)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username