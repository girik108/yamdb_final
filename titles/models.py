from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models


def get_year():
    return date.today().year


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return f'{self.name} - {self.slug}'


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return f'{self.name} - {self.slug}'


class Title(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    year = models.PositiveIntegerField(
        default=get_year,
        validators=[MaxValueValidator(get_year), ],
        db_index=True)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='titles',
                                 db_index=True)
    genre = models.ManyToManyField(Genre, related_name='titles',
                                   db_index=True)
