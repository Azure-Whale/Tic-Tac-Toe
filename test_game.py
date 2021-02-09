#test_game.py
from app import TicTacToe

def test_col_win():
    """
    Testing if a player can win when the player has three marker on same column
    """
    game = TicTacToe()
    game.choose_game_mode('o')
    game.place_marker('o',0,0)
    game.place_marker('x',0,1)
    game.place_marker('o',1,0)
    game.place_marker('x',0,2)
    game.place_marker('o',2,0)
    game.print_board()
    assert game.current_statue == game.STATES.NAUGHT_WON

def test_row_win():
    """
    Testing if a player can win when the player has three marker on same row
    """
    game = TicTacToe()
    game.choose_game_mode('x')
    game.place_marker('x',0,0)
    game.place_marker('o',0,1)
    game.place_marker('x',1,0)
    game.place_marker('o',0,2)
    game.place_marker('x',2,0)
    game.print_board()
    assert game.current_statue == game.STATES.CROSS_WON

def test_diagrame_win():
    """
    Testing if a player can win when the player has three marker on same diagrame
    """
    game = TicTacToe()
    game.choose_game_mode('x')
    game.place_marker('x',0,1)
    game.place_marker('o',1,1)
    game.place_marker('x',0,2)
    game.place_marker('o',2,2)
    game.place_marker('x',1,2)
    game.place_marker('o',0,0)
    game.print_board()
    assert game.current_statue == game.STATES.NAUGHT_WON

def test_draw():
    """
    Testing if the game can draw correctly when the board is full and no one wins
    """
    game = TicTacToe()
    game.choose_game_mode('o')
    game.place_marker('o',0,0)
    game.place_marker('x',0,1)
    game.place_marker('o',0,2)
    game.place_marker('x',1,1)
    game.place_marker('o',1,0)
    game.place_marker('x',2,0)
    game.place_marker('o',1,2)
    game.place_marker('x',2,2)
    game.place_marker('o',2,1)
    game.print_board()
    assert game.current_statue == game.STATES.DRAW


def test_game_mode():
    """
    Testing if the game can choose the turn according to user input correctly
    """
    game = TicTacToe()
    game.choose_game_mode('o')
    assert game.current_statue == game.STATES.NAUGHT_TURN
    game.choose_game_mode('x')
    assert game.current_statue == game.STATES.CROSS_TURN
