from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(
        User, related_name="notifications", on_delete=models.CASCADE
    )
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Notification for {self.user.username}"
