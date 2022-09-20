from django.db import models
from simple_history.models import HistoricalRecords

from pieces import managers


class Piece(models.Model):
    class TypeChoices(models.IntegerChoices):
        KING = 1, 'King'
        QUEEN = 2, 'Queen'
        ROOK = 3, 'Rook'
        BISHOP = 4, 'Bishop'
        KNIGHT = 5, 'Knight'
        PAWN = 6, 'Pawn'

        def __str__(self):
            return self.label

    class ColorChoices(models.IntegerChoices):
        BLACK = 1, 'Black'
        WHITE = 2, 'White'

        def __str__(self):
            return self.label

    id = models.AutoField(primary_key=True)
    type = models.IntegerField(
        null=False,
        choices=TypeChoices.choices
    )
    color = models.IntegerField(
        null=False,
        choices=ColorChoices.choices
    )

    history = HistoricalRecords()
    objects = managers.PieceManager()

    class Meta:
        ordering = ['-id']
        db_table = 'piece'
        verbose_name = 'Piece'
