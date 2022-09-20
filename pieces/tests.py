import json
from os.path import join

from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import APIClient

from chess_board import settings
from pieces.models import Piece
from pieces.viewsets import PieceViewSet


class PieceTest(TestCase):
    @staticmethod
    def create_piece(type=1, color=1):
        return Piece.objects.create(type=type, color=color)

    def test_piece_creation(self):
        instance = self.create_piece()
        self.assertTrue(isinstance(instance, Piece))


class PieceViewSetTest(TestCase):
    fixtures = [
        'pieces'
    ]
    path = join(str(settings.BASE_DIR), 'pieces/fixtures/')

    for file in fixtures:
        print(f"{path}{file}.json")

    def setUp(self):
        self.request = RequestFactory()
        self.piece = Piece.objects.create(type=1, color=1)

    def test_piece_list(self):
        request = self.request.get('chess-board/pieces')
        response = PieceViewSet.as_view({'get': 'list'})(request)
        response = response.data['results'][0]
        self.assertEqual(response['type'], 'King')
        self.assertEqual(response['color'], 'Black')

    def test_piece_create(self):
        data = json.dumps({
            'type': Piece.TypeChoices.KNIGHT,
            'color': Piece.ColorChoices.BLACK
        })
        client = APIClient()
        response = client.post('/chess-board/pieces/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = response.data
        self.assertEqual(response['type'], 'Knight')
        self.assertEqual(response['color'], 'Black')

    def test_piece_movement(self):
        data = {
            'piece_id': 1,
            'coordinate': 'h1'
        }
        expected_response = ["g3", "f2"]
        response = self.client.get(f"/chess-board/pieces/get-movement/?coordinate={data['coordinate']}&piece_id={data['piece_id']}")
        self.assertListEqual(response.data['locations'], expected_response)
