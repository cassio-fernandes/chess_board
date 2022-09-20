from django.contrib import admin

from pieces.models import Piece


@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    fields = ['type', 'color']
    list_display = ['type', 'color']
