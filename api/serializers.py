from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from api.models import Wall, PostLike, PostComment
from django.core.mail import send_mail
from django.conf import settings


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        try:
            send_mail(
                'Welcome to The Wall',
                'Hello %s, Thank you for joining us.' % user.username,
                settings.FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
        except:
            print("email failed")

        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class WallSerializer(ModelSerializer):
    user = SerializerMethodField()
    likes = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Wall
        fields = [
            'id', 'message', 'user', 'image', 'likes', 'comments', 'date_created', 'date_modified',
        ]
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_likes(self, obj):
        likes = obj.likes.all()
        if likes:
            return PostLikeSerializer(likes, many=True).data

        return []

    def get_comments(self, obj):
        comments = obj.comments.all()
        if comments:
            return PostCommentSerializer(comments, many=True).data

        return []


class PostLikeSerializer(ModelSerializer):
    user = SerializerMethodField()
    wall_id = SerializerMethodField()

    class Meta:
        model = PostLike
        fields = [
            'id', 'user', 'wall_id', 'date_created', 'date_modified',
        ]
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_wall_id(self, obj):
        return obj.wall.id


class PostCommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    wall_id = SerializerMethodField()

    class Meta:
        model = PostComment
        fields = [
            'id', 'user', 'wall_id', 'message', 'date_created', 'date_modified',
        ]
        extra_kwargs = {'date_created': {'read_only': True}, 'date_modified': {'read_only': True}}

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_wall_id(self, obj):
        return obj.wall.id
