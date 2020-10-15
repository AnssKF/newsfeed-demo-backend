from django.urls import path, include
from rest_framework import routers
from django.conf import settings

from .views import *


#---
if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register('user/signup', SignupViewSet, 'signup')
router.register('user/login', LoginViewSet, 'login')