from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from api.views import RegistrationApiView, WallApiView, PostLikeApiView, PostCommentApiView


urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^register/$', RegistrationApiView.as_view(), name='register'),
    url(r'^walls(/?)$', WallApiView.as_view(), name='walls'),
    url(r'^walls/(?P<id>\d+)/likes/$', PostLikeApiView.as_view(), name='likes'),
    url(r'^walls/(?P<id>\d+)/comments/$', PostCommentApiView.as_view(), name='comments'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
