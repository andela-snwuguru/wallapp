from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


def get_object_by_api_view(view, object_name):
    id = view.kwargs.get('id',0)
    return get_object_or_404(
        object_name,
        id=int(id)
    )