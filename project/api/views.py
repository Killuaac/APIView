from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView,
                                     CreateAPIView,
                                     ListAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser, AllowAny)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .models import Message, User
from .serializer import (MessageSerializer, RegistrationSerializer,
                         LoginSerializer)
from .permissions import IsAdminOrReadOnly


class MessageList(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdate(RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDestroy(RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class Registration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=201)
        return Response({'error': serializer.errors}, status=400)


class Login(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response('Invalid credentials', status=400)
        user = serializer.validated_data
        print(user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=201)
        return Response({'error': serializer.errors}, status=400)


@api_view(['GET'])
def logout(request):
    if not request.user.is_active:
        return Response({"error": {'code': 403,
                                   "message": "Login failed"}}, status=403)
    request.user.auth_token.delete()
    return Response({"data": {'message': "Log out"}}, status=200)
