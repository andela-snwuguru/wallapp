from django.contrib.auth.models import User
from api.serializers import UserSerializer, WallSerializer, PostLikeSerializer, PostCommentSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from api.permissions import AllowAllForGet
from api.models import Wall, PostLike, PostComment
from .utils import get_object_by_api_view
from rest_framework.serializers import ValidationError



class RegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class WallApiView(ListCreateAPIView):

    """
    Returns list of walls if you are doing a GET request.
    Creates new wall if you are doing a POST request.
    """

    queryset = Wall.objects.order_by('-date_created').all()
    serializer_class = WallSerializer
    permission_classes = [AllowAllForGet]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


class PostLikeApiView(ListCreateAPIView):

    """
    Returns list of post likes if you are doing a GET request.
    Creates new post like if you are doing a POST request.
    """

    serializer_class = PostLikeSerializer
    permission_classes = [AllowAllForGet]

    def perform_create(self, serializer):
        post = get_object_by_api_view(self, Wall)
        like = PostLike.objects.filter(user=self.request.user, wall=post)
        if like:
            raise ValidationError({"error":"Integrity constraint"})

        serializer.save(user=self.request.user, wall=post)
        return serializer

    def get_queryset(self):
        post = get_object_by_api_view(self, Wall)
        return PostLike.objects.filter(wall=post)


class PostCommentApiView(ListCreateAPIView):

    """
    Returns list of post comments if you are doing a GET request.
    Creates new post comment if you are doing a POST request.
    """

    serializer_class = PostCommentSerializer
    permission_classes = [AllowAllForGet]

    def perform_create(self, serializer):
        post = get_object_by_api_view(self, Wall)
        serializer.save(user=self.request.user, wall=post)
        return serializer

    def get_queryset(self):
        post = get_object_by_api_view(self, Wall)
        return PostComment.objects.filter(wall=post)