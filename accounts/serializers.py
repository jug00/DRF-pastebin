from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer as _LoginSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["url", "id", "username", "email", "snippets"]
        extra_kwargs = {
            "url": {"view_name": "user-detail", }
        }


class LoginSerializer(_LoginSerializer):
    username = None
    password = serializers.CharField(style={'input_type': 'password'}, required=True)
    email = serializers.EmailField(required=True, allow_blank=False)


class EmailConfirmSerializer(serializers.Serializer):
    key = serializers.CharField(read_only=True)
    url = serializers.URLField(read_only=True)

