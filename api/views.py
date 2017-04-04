from django.contrib.auth.models import User
from api.serializers import UserSerializer, WallSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from api.permissions import AllowAllForGet
from api.models import Wall


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
