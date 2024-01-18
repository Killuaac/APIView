from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView, ListAPIView,
                                     CreateAPIView)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializer import (StudentSerializer, SubjectSerializer, ClassSerializer,
                         RegistrationSerializer, LoginSerializer)
from .models import Class, Subject, Students


class CreateStudentView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class CreateSubjectView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CreateClassView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class DeleteOrUpdateStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class DeleteOrUpdateSubjectView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DeleteOrUpdateClassView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class Registration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

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