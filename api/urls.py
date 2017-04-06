from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from api.views import RegistrationApiView, WallApiView, PostLikeApiView


urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^register/$', RegistrationApiView.as_view(), name='register'),
    url(r'^walls(/?)$', WallApiView.as_view(), name='walls'),
    url(r'^walls/(?P<id>\d+)/likes/$', PostLikeApiView.as_view(), name='likes'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
