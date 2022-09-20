import string


class ChessBoard:
    def __init__(self):
        self.columns = string.ascii_lowercase[:8]
        self.rows = string.digits[-2:0:-1]
        self.board = self._make_board()

    def _make_board(self):
        board = {}
        index_row = 0
        while index_row < 8:
            _row = int(self.rows[index_row])
            _cols = {c: f'{c}{_row}' for c in self.columns}
            board.update({_row: _cols})
            index_row += 1
        return board


class PieceMovement:
    chess = ChessBoard()

    @staticmethod
    def king(location):
        return []

    @staticmethod
    def queen(location):
        return []

    @staticmethod
    def rook(location):
        return []

    @staticmethod
    def knight(coordinate):
        column, row = coordinate
        row = int(row)
        movements = []

        def next_position(data, origin, increment):
            try:
                return data[origin + increment]
            except (KeyError, IndexError):
                return None

        def previous_position(data, origin, decrement):
            try:
                index = origin - decrement
                # check to prevent list slicing
                if index >= 0:
                    return data[index]
                return None
            except (KeyError, IndexError):
                return None

        def columns(current_row):
            right = next_position(data=PieceMovement.chess.columns, origin=column_origin, increment=1)
            left = previous_position(data=PieceMovement.chess.columns, origin=column_origin, decrement=1)

            return [current_row.get(right), current_row.get(left)]

        def rows(current_column):
            up = next_position(data=PieceMovement.chess.board, origin=row, increment=1)
            down = previous_position(data=PieceMovement.chess.board, origin=row, decrement=1)
            _columns = []

            if up:
                _columns.append(up.get(current_column))

            if down:
                _columns.append(down.get(current_column))

            return _columns

        column_origin = PieceMovement.chess.columns.index(column)
        row_origin = PieceMovement.chess.board.get(row)

        if row_origin and column_origin >= 0:
            row_above = next_position(data=PieceMovement.chess.board, origin=row, increment=2)
            row_below = previous_position(data=PieceMovement.chess.board, origin=row, decrement=2)
            column_right = next_position(data=PieceMovement.chess.columns, origin=column_origin, increment=2)
            column_left = previous_position(data=PieceMovement.chess.columns, origin=column_origin, decrement=2)

            if row_above:
                movements.extend(columns(row_above))

            if row_below:
                movements.extend(columns(row_below))

            if column_right:
                movements.extend(rows(column_right))

            if column_left:
                movements.extend(rows(column_left))

        return list(filter(lambda x: x is not None, movements))
