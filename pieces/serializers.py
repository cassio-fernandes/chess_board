from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pieces import models
from pieces.fields import CustomChoiceField
from shared import rules


class PieceSerializer(serializers.ModelSerializer):
    type = CustomChoiceField(choices=models.Piece.TypeChoices)
    color = CustomChoiceField(choices=models.Piece.ColorChoices)

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


class PieceMovement(serializers.Serializer):
    piece_id = PieceSerializer(required=False)
    coordinate = serializers.CharField(max_length=2)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
