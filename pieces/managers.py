from django.db import models
from django.db.models import Count


class PieceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def count_pieces_by_color(self, piece_type, color):
        return self.get_queryset().filter(
            type=piece_type,
            color=color
        ).aggregate(
            count_pieces=Count('color')
        )
