from django.urls import path, include
from rest_framework import routers
from django.conf import settings

from .views import *


#---
if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register('post', PostViewSet, 'post')
router.register('comment', CommentViewSet, 'comment')
router.register('like', LikeViewSet, 'like')