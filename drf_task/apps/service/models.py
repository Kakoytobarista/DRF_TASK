from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Property(models.Model):
    key = models.CharField(max_length=155,
                           verbose_name='Key of property')
    value = models.CharField(max_length=155,
                             verbose_name='Value of property')

    def __str__(self):
        return f'{self.key} : {self.value}'


class Entity(models.Model):
    modified_by = models.ForeignKey(to=User,
                                    on_delete=models.SET_DEFAULT,
                                    default=None,
                                    related_name='entity',
                                    verbose_name='Creator')
    value = models.IntegerField(verbose_name='Value of object',
                                validators=(
                                    MinValueValidator(1, 'Too small value'),
                                    MaxValueValidator(9999, 'Too big value '),
                                ))
    properties = models.ManyToManyField(to=Property,
                                        related_name='properties',
                                        blank=True,
                                        verbose_name='Properties of object')

    def __str__(self):
        return f'Author:{self.modified_by} | Value: {self.value} | Property: {self.properties}'
