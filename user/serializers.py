from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken, api_settings

from .models import CustomUserModel


class RegisterUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUserModel
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

        read_only_fields = ('id',)

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.pop('password2', None)
        if password2 != password1:
            raise ValidationError(_('Passwords did not match.'))
        return super().validate(attrs)

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        user = CustomUserModel(**validated_data)
        user.set_password(password1)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['user'] = UserSerializer(self.user).data
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ('id', 'email', 'full_name')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ('id', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)
