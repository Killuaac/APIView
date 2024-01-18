from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        else:
            return False


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError('Your passwords do not match')

        user.set_password(password)
        user.save()
        return user
