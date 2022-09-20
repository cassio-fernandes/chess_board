import json

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pieces import serializers, models
from pieces.actions import PieceMovement


class PieceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PieceSerializer
    queryset = models.Piece.objects.all()

    @action(methods=['GET'], detail=False, url_path='get-movement')
    def get_movement(self, request):
        data = request.query_params
        serializer = serializers.PieceMovement(data=data)
        serializer.is_valid(raise_exception=True)
        data = PieceMovement.knight(**serializer.data)

        return Response(data={'locations': data}, status=200)
