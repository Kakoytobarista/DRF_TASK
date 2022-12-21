from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserSerializer

from django.contrib.auth import get_user_model

from apps.service.models import Entity, Property


User = get_user_model()


class EntitySerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(required=False)

    def to_internal_value(self, data):
        field_value = data.get('data[value]')
        value = field_value if field_value is not None else data.get('value')
        data['value'] = value
        return super().to_internal_value(data)

    class Meta:
        model = Entity

        fields = (
            'value',
            'properties',
        )


class EntityRetrieveSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    def get_properties(self, obj):
        properties = obj.properties.all()
        return {prop.key: prop.value for prop in properties}

    class Meta:
        model = Entity

        fields = (
            'value',
            'properties',
        )


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property

        fields = (
            'key',
            'value',
        )


class CustomUserSerializer(DjoserSerializer):

    class Meta:
        model = User

        fields = (
            'username',
            'password',
        )
