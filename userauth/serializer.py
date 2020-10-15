from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import fields
from rest_framework.validators import UniqueValidator

#---
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['id', 'email', 'username']


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        required=True,
        min_length=8)


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model=User
        fields = ('id', 'username', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8)

    class Meta:
        model=User
        fields = ('email', 'password')