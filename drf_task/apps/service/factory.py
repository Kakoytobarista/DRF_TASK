import factory
from django.contrib.auth import get_user_model

from apps.service.models import Property, Entity

User = get_user_model()


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    key = factory.Faker('name')
    value = factory.Faker('job')


class EntityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entity

    modified_by = factory.Iterator(User.objects.all())
    value = factory.Faker('random_int')

    @factory.post_generation
    def properties(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.properties.add(group)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')


# UserFactory.create_batch(5)
# PropertyFactory.create_batch(5)
# EntityFactory.create_batch(5)
