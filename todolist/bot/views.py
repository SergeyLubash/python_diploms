from django.shortcuts import render
import os
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from .models import TgUser
from .serializers import TgUserSerializer
from .tg.client import TgClient


class BotVerifyView(generics.UpdateAPIView):
    model = TgUser
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        data = self.serializer_class(request.data).data
        tg_client = TgClient(os.environ.get('TG_BOT_API_TOKEN'))
        tg_user = TgUser.objects.filter(verification_code=data['verification_code']).first()
        if not tg_user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        tg_user.user = request.user
        tg_user.save()
        tg_client.send_message(chat_id=tg_user.tg_chat_id, text='Успешно')
        return Response(data=data, status=status.HTTP_201_CREATED)
