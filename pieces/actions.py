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
        column, row = location
        row = int(row)
        vertical = []
        horizontal = []
        movements = []

        if row - 1 >= 1:
            vertical.append(row - 1)

        vertical.append(row)

        if row + 1 < 8:
            vertical.append(row + 1)

        column_index = PieceMovement.chess.columns.index(column)

        if column_index - 1 >= 1:
            horizontal.append(PieceMovement.chess.columns[column_index - 1])

        horizontal.append(PieceMovement.chess.columns[column_index])

        if column_index + 1 < 8:
            horizontal.append(PieceMovement.chess.columns[column_index + 1])

        for r in vertical:
            movements.append([PieceMovement.chess.board[r][c] for c in horizontal if PieceMovement.chess.board[r][c] != location])

        return movements

    @staticmethod
    def queen(location):
        movements = []
        for row in PieceMovement.chess.rows:
            row = int(row)
            movements.append([PieceMovement.chess.board[row][col] for col in PieceMovement.chess.columns if PieceMovement.chess.board[row][col] != location])
        # return movements
        [print(m) for m in movements]

    @staticmethod
    def rook(location):
        column, row = location
        row = int(row)
        return [[PieceMovement.chess.board[row][col] for col in PieceMovement.chess.board[int(row)] if PieceMovement.chess.board[row][col] != location],
                [PieceMovement.chess.board[int(r)][column] for r in PieceMovement.chess.rows if PieceMovement.chess.board[int(r)][column] != location]]

    @staticmethod
    def knight(location):
        column, row = location
        row = int(row)
        movements = []

        def get_next(data, _target, increment):
            try:
                return data[_target + increment]
            except IndexError:
                return data[_target]

        def get_previous(data, _target, decrement):
            try:
                return data[_target - decrement]
            except IndexError:
                return data[_target]

        target = PieceMovement.chess.columns.index(column)
        if row + 2 <= 8:
            _current_location = get_next(data=PieceMovement.chess.board, _target=row, increment=2)
            if target + 1 < 8:
                movements.append(_current_location[get_next(data=PieceMovement.chess.columns, _target=target, increment=1)])

            if target - 1 >= 1:
                movements.append(_current_location[get_previous(data=PieceMovement.chess.columns, _target=target, decrement=1)])

        if row - 2 >= 1:
            _current_location = get_previous(data=PieceMovement.chess.board, _target=row, decrement=2)
            if target + 1 < 8:
                movements.append(_current_location[get_next(data=PieceMovement.chess.columns, _target=target, increment=1)])

            if target - 1 >= 1:
                movements.append(_current_location[get_previous(data=PieceMovement.chess.columns, _target=target, decrement=1)])

        if target + 2 <= 8:
            if row + 1 < 8:
                _current_location = get_next(data=PieceMovement.chess.board, _target=row, increment=1)
                movements.append(_current_location[get_next(data=PieceMovement.chess.columns, _target=target, increment=2)])

            if row - 1 >= 1:
                _current_location = get_previous(data=PieceMovement.chess.board, _target=row, decrement=1)
                movements.append(_current_location[get_next(data=PieceMovement.chess.columns, _target=target, increment=2)])

        if target - 2 >= 1:
            if row - 1 >= 1:
                _current_location = get_previous(data=PieceMovement.chess.board, _target=row, decrement=1)
                movements.append(_current_location[get_previous(data=PieceMovement.chess.columns, _target=target, decrement=2)])

            if row + 1 < 8:
                _current_location = get_next(data=PieceMovement.chess.board, _target=row, increment=1)
                movements.append(_current_location[get_previous(data=PieceMovement.chess.columns, _target=target, decrement=2)])

        return movements
