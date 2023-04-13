CHESS BOARD
--

A chessboard is the type of checkerboard used in the board game chess, consisting of 64
squares (eight rows and eight columns). The squares are arranged in two alternating colors
(light and dark). <https://en.wikipedia.org/wiki/Chessboard>

The API receive the piece type/name and the color and return the piece id;

The API receive a cell coordinate (in Algebraic notation) and return an array
with all possible locations where the knight can move within 2 turns.

---

REQUIREMENTS:
* Linux
* Python 3.10.*

create virtualenv:    `$ python -m venv venv`

activate virtualenv:  `$ source venv/bin/activate`

install requirements: `$ pip install -r requirements`

run migrations:       `$ python manage.py migrate`

run application:      `$ python runserver 127.0.0.1:8000`

_________

EXECUTE TESTS: 

* `$ coverage run manage.py test pieces/ -v 2`