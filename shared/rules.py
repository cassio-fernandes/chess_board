KING = 'King'
QUEEN = 'Queen'
ROOK = 'Rook'
BISHOP = 'Bishop'
KNIGHT = 'Knight'
PAWN = 'Pawn'

MAX_PIECES = {
    KING: 1,
    QUEEN: 1,
    ROOK: 2,
    BISHOP: 2,
    KNIGHT: 2,
    PAWN: 8,
}

KING_MOVEMENT = {
    'top': 1,
    'right': 1,
    'bottom': 1,
    'left': 1,
    'top_right': 1,
    'bottom_right': 1,
    'bottom_left': 1,
    'top_left': 1,
}
QUEEN_MOVEMENT = {
    'top': 8,
    'right': 8,
    'bottom': 8,
    'left': 8,
    'top_right': 8,
    'bottom_right': 8,
    'bottom_left': 8,
    'top_left': 8,
}
ROOK = {
    'top': 8,
    'right': 8,
    'bottom': 8,
    'left': 8,
    'top_right': 0,
    'bottom_right': 0,
    'bottom_left': 0,
    'top_left': 0,
}
BISHOP = {
    'top': 0,
    'right': 0,
    'bottom': 0,
    'left': 0,
    'top_right': 8,
    'bottom_right': 8,
    'bottom_left': 8,
    'top_left': 8,
}
KNIGHT = {
    'top': 0,
    'right': 0,
    'bottom': 0,
    'left': 0,
    'top_right': 8,
    'bottom_right': 8,
    'bottom_left': 8,
    'top_left': 8,
}
