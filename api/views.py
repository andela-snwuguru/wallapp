from django.contrib.auth.models import User
from api.serializers import UserSerializer, WallSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from api.models import Wall


class RegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class WallApiView(ListAPIView):

    """
    Returns list of walls if you are doing a GET request.
    Creates new wall if you are doing a POST request.
    """

    serializer_class = WallSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Wall.objects.all()