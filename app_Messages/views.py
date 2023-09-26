from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import BaseParser
from .models import Messages
from app_CustomUser import models
from rest_framework import status
import requests
from django.conf import settings

class PlainTextParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()
    

@api_view(['POST'])
@parser_classes([PlainTextParser])
@permission_classes([IsAuthenticated])
def send_messages(request):
    user = request.user
    chat_id = user.chat_id
    text = request.data
    text = text.decode('utf-8')
    print(text)
    message = Messages(text=text, user=user)
    message.save()
    if not chat_id:
        chat_id = user.request_chat_id()
        if not chat_id:
            return Response(status=status.HTTP_403_FORBIDDEN)
    a = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}').json()     
    print(a)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    message = Messages.objects.filter(user=request.user).values()
    message_return = []
    if message:
        for i in message:
            message_return.append({
                "сообщение": i['text'],
                "дата": i['datetime'].strftime('%Y-%m-%d %H:%M:%S')
            })
    return Response({'messages': message_return})

