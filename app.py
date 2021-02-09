from enum import Enum 
import logging
from random import choice

logging.basicConfig(filename='Logs/game.log', level=logging.DEBUG)

class TicTacToe: 
    class STATES(Enum): 
        CROSS_TURN = 0 
        NAUGHT_TURN = 1 
        DRAW = 2 
        CROSS_WON = 3 
        NAUGHT_WON = 4 

    def __init__(self):
        # Customize the game setting
        self.setting = {
                'first': None, # the first player will be decided by its value
        }
        # init the game board, '_' marks the free place, 'o' marks the places hold by o, 'x' marks the places hold by x
        self.board = [['_' for row in range(3)] for col in range(3)]
        # init the game statue and max available places
        self.current_statue = None
        self.remain_places = 9
        logging.info('Game Ready')
    
    def choose_game_mode(self,mode = None):
        """
        The func helps the player input who is the first according to given mode, otherwise it would be random
        """
        if mode == 'o':
            self.setting['first'] = 'o'
            self.current_statue = self.STATES.NAUGHT_TURN
        elif mode == 'x':
            self.setting['first'] = 'x'
            self.current_statue = self.STATES.CROSS_TURN
        else:
            self.setting['first'] = choice(['o','x'])
            self.current_statue = self.choose_game_mode(self.setting['first'])

    def place_marker(self, symbol, row, column):
        """
        According to given sympol and coordinate, the func will try to place a marker to target place
        """
        # if the game is over, operation is invaild.
        if self.current_statue in {self.STATES.DRAW,self.STATES.CROSS_WON,self.STATES.NAUGHT_WON}:
            logging.warning('Invaild operation, the game is over.')
            return
        # if target place is used, operation is invaild.
        if self.board[row][column] != '_':
            logging.warning('Invaild operation, the place has been hold by {}'.format(self.board[row][column]))
            return
        # if the player plays in correct turn, place a new marker in available target place and update game statue
        if symbol == 'x' and self.current_statue==self.STATES.CROSS_TURN:
            self.board[row][column] = 'x'
            self.update_game('x',row,column)
        elif symbol == 'o' and self.current_statue==self.STATES.NAUGHT_TURN:
            self.board[row][column] = 'o'
            self.update_game('o',row,column)
        # if the player plays when it is not his/her turn, the operation is invaild
        else:
            logging.warning('Invaild operation, the game is played in turns! Current player is {}'.format(self.current_statue))
            return
    
    def update_game(self,symbol,row,column):
        # the available places minus 1 when a new marker placed
        self.remain_places -= 1
        
        """Check conditions which may create a winner"""
        # check if the new marker forms a row having three same symbol
        def check_row():
            cnt = 0
            for i in range(3):
                if self.board[i][column] == symbol:
                    cnt += 1
            return True if cnt ==3 else False
        # check if the new marker forms a column having three same symbol
        def check_col():
            cnt = 0
            for i in range(3):
                if self.board[row][i] == symbol:
                    cnt += 1
            return True if cnt == 3 else False
        # check if the new marker forms a diagonal having three same symbol
        def check_diagonal():
            cnt1 = cnt2 = 0
            row = list(range(3))
            col = list(range(3))
            for i,j in zip(row,col):
                if self.board[i][j] == symbol:
                    cnt1 += 1
            for i,j in zip(row,col[::-1]):
                if self.board[i][j] == symbol:
                    cnt2 += 1
            return True if max(cnt1,cnt2) == 3 else False

        """According to current board, update game statue"""
        # if there is no winner for now
        if not (check_row() or check_col() or check_diagonal()):
            # if the game run out of places, then draw this game
            if self.remain_places == 0:
                self.current_statue = self.STATES.DRAW
                logging.info('Game Over, players draw.. ')
            # if there still are available places, next plyaer will play
            elif self.current_statue == self.STATES.NAUGHT_TURN:
                self.current_statue = self.STATES.CROSS_TURN
                logging.info('Cross moves ')
            else:
                self.current_statue = self.STATES.NAUGHT_TURN
                logging.info('Naught moves ')
        # if there is a winner
        else:
            # player in current turn will win the game
            if self.current_statue == self.STATES.NAUGHT_TURN:
                self.current_statue = self.STATES.NAUGHT_WON
                logging.info('Game Over, cross wins.. ')
            elif self.current_statue == self.STATES.CROSS_TURN:
                self.current_statue = self.STATES.CROSS_WON
                logging.info('Game Over, naguht wins.. ')
        return self.current_statue
        

    def print_board(self):
        """
        If there is a need to print out the board, call this func
        """
        for row in self.board:
            print(row)
