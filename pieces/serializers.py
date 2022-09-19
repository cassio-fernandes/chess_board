from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pieces import models
from shared import rules


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Piece
        fields = '__all__'

    def validate(self, attrs):
        def _max_piece_type():
            instance = models.Piece
            pieces = instance.objects.count_pieces_by_color(_type, _color)

            return pieces.get('count_pieces') == rules.MAX_PIECES[str(instance.TypeChoices(_type))]

        _type = attrs.get('type')
        _color = attrs.get('color')

        if _max_piece_type():
            raise ValidationError(detail='Limit of piece(s) exceeded')

        return attrs

    def create(self, validate_data):
        instance = models.Piece(
            type=validate_data.get('type'),
            color=validate_data.get('color')
        )
        instance.save()
        return instance

    def update(self, instance: models.Piece, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
