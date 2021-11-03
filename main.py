import sys
import time
from PyQt5.QtWidgets import *
import OctiModel.BoardGame
import OctiView.BoardGameView
import OctiController.BoardGameController
from OctiModel.Enums import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    board = OctiModel.BoardGame.BoardGame()
    view = OctiView.BoardGameView.BoardGameView(board)
    controller = OctiController.BoardGameController.BoardGameController(board, view)
    board.printBoard()
    board.insertArrow('G1', Directions.Down)
    #view.repaint()
    #time.sleep(1)
    board.insertArrow('R1', Directions.Up)
    #view.repaint()
    #time.sleep(1)
    board.insertArrow('R1', Directions.UpLeft)
    #view.repaint()
    #time.sleep(1)
    board.insertArrow('G2', Directions.DownLeft)
    #view.repaint()
    #time.sleep(1)
    board.move('R1', (4, 1))
    board.printBoard()
    #view.repaint()
    #time.sleep(1)
    board.move('G2', (2, 1))
    board.printBoard()
    #view.repaint()
    #time.sleep(1)
    board.insertArrow('R3', Directions.Up)
    #view.repaint()
    #time.sleep(1)
    board.insertArrow('G1', Directions.Right)
    #view.repaint()
    #time.sleep(1)
    board.move('R3', (4, 3))
    board.printBoard()
    print(board.whereToGo('G1'))

    jsonBoard = board.boardToJson()
    print(jsonBoard)
    board.jsonToBoard(jsonBoard)
    sys.exit(app.exec_())









