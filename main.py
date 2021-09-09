import OctiModel.BoardGame
from OctiModel.Enums import *

if __name__ == '__main__':

    board = OctiModel.BoardGame.BoardGame()
    board.printBoard()
    board.insertArrow('G1', Directions.Down)
    board.insertArrow('R1', Directions.Up)
    board.insertArrow('R1', Directions.UpLeft)
    board.insertArrow('G2', Directions.DownLeft)
    board.move('R1', 4, 1)
    board.printBoard()
    board.move('G2', 2, 1)
    board.printBoard()
    board.insertArrow('R3', Directions.Up)
    board.insertArrow('G1', Directions.Right)
    board.move('R3', 4, 3)
    board.printBoard()
    print(board.whereToGo('G1'))




