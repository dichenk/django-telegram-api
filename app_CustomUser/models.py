from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import requests



class CustomUser(AbstractUser):
    username = models.CharField(max_length=1024, unique=True)
    password = models.CharField(max_length=1024, unique=True)
    chat_id = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    

    def request_chat_id(self):
        if not self.chat_id:
            updates = requests.get(f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/getUpdates").json()
            matching_ids = [entry['message']['from']['id'] for entry in updates['result'] if entry['message']['from']['username'] == self.username]
            
            if matching_ids:
                self.chat_id = matching_ids[0]
                self.save()
                return self.chat_id
        return None

    def save(self, *args, **kwargs):
        self.request_chat_id()
        return super().save(*args, **kwargs)


