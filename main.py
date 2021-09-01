import OctiModel.BoardGame
from OctiModel.Enums import *

if __name__ == '__main__':

    board = OctiModel.BoardGame.BoardGame()
    board.printBoard()
    board.insertArrow('G1', Directions.Down)
    board.insertArrow('R2', Directions.Up)
    board.whereToGo('G1')


