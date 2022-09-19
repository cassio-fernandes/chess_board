from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pieces import serializers, models


class PieceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PieceSerializer
    queryset = models.Piece.objects.all()

    @action(methods=['GET'], detail=False, url_path='get-movement')
    def get_movement(self, request):
        a = 1
        return Response(data={'message': 'Ok'})
