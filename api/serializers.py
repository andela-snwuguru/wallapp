from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from api.models import Wall


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class WallSerializer(ModelSerializer):
    class Meta:
        model = Wall
        fields = [
            'id', 'message', 'user', 'image', 'date_created', 'date_modified',
        ]
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}
