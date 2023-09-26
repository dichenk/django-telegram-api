from django.db import models

from app_CustomUser.models import CustomUser

class Messages(models.Model):
    text = models.CharField(max_length=1024)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Message {self.text}'