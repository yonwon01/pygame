#run.py
from ..graphic import screen
from ..sound import echo


def test_start():
    print('start called')
    screen.test_screen()
    echo.test_echo()