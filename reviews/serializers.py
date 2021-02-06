from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import (CurrentUserDefault, ModelSerializer,
                                        SlugRelatedField)

from titles.models import Title

from .models import Review


class ReviewSerializer(ModelSerializer):
    title = SlugRelatedField(slug_field='name', read_only=True)
    author = SlugRelatedField(default=CurrentUserDefault(),
                              slug_field='username', read_only=True)

    def validate(self, data):
        request = self.context['request']
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)

        if request.method == 'POST' and Review.objects.filter(
                title=title, author=request.user
        ).exists():
            raise ValidationError(
                'Пользователь может оставить только один отзыв на один объект.')

        return data

    class Meta:
        model = Review
        fields = '__all__'
