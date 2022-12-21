from django.urls import include, path
from rest_framework import routers

from apps.api.views import EntityViewSet, PropertyViewSet, CustomUserViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('entity', EntityViewSet, basename='entity')
router.register('property', PropertyViewSet, basename='property')
router.register('users', CustomUserViewSet, basename='users')


urlpatterns = (
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
)
