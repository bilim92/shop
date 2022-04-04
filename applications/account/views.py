from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = 'ВЫ УСПЕШНО ЗАРЕГИСТРИРОВАНЫ. ВАМ ОТПРАВЛЕНО ПИСЬМО'
            return Response(message, status=201)
        return Response(status=status.HTTP_404_BAD_REQUEST)
