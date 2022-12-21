from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated

from djoser.views import UserViewSet as DjoserViewSet

from django.contrib.auth import get_user_model

from apps.api.serializers import EntitySerializer, PropertySerializer, \
    CustomUserSerializer, EntityRetrieveSerializer
from apps.service.models import Entity, Property

User = get_user_model()


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)

    def get_serializer_class(self):
        """Разделил сериализаторы на получение данных и изменение
        для лучшей читаемости и разделения сериализаторов к области 2 и 3 задач"""
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            print("POST")
            return EntitySerializer
        print("GET")
        return EntityRetrieveSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CustomUserViewSet(DjoserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )
