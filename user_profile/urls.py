from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]