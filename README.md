# Tic-Tac-Toe
It's a private assesment submission from Kezheng

The game doesn't have an AI, it realizes the logic of the Tic-Tac-Toe. symbol can be "x" or "o", row and column can be an integer from 0 to 2. The empty place of board would be marked as "-". Once there are three same markers on any row, column or diagonal, one player would win the game, otherwise the game would draw or continue.


## **Local Development Setup**
1. Install Git and clone the repo.

2. Set given env as your development env.

## **Files**
1. app.py
```
It contains Tic-Tac-Toe main object and all the methods within it. 
```
2. requirements.py
```
It records all the dependencies
```
3. test_game.py
```
It is used for conducting unittest
```
4. Log
```
It contains the running progress log of this game
```
## **Functions**
1.  **def choose_game_mode(self,symbol = None)**
```
The func helps the player input who is the first according to given mode, otherwise it would be random

Parameters:

@symbol: the symbol who is going to play first
```

2.  **def place_marker(self, symbol, row, column)**
```
According to given sympol and coordinate, the func will try to place a marker to target place

Parameters:

@symbol: the symbol who is going to play first

@row: the index of row of targe place

@column: the index of column of targe place
```
3.  **def update_game(self,symbol,row,column)**
```
Update the current game statue according to tic-tac-toe game rules

Parameters:

@symbol: the symbol who is going to play first

@row: the index of row of most recently placed marker

@column: the index of column of most recently placed marker
```
4.  **def print_board(self)**
```
If there is a need to print out the board, call this func
```
