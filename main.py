import sys
import time
from PyQt5.QtWidgets import *
import OctiModel.BoardGame
import OctiView.BoardGameView
import OctiController.BoardGameController
import OctiAi.OctiAi_alphaBeta
from OctiModel.Enums import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    board = OctiModel.BoardGame.BoardGame()
    AiBoard = OctiModel.BoardGame.BoardGame()
    AI = OctiAi.OctiAi_alphaBeta.OctiAi_alphaBeta(AiBoard)
    view = OctiView.BoardGameView.BoardGameView(board)
    controller = OctiController.BoardGameController.BoardGameController(board, view, AI)
    controller.playAgainstAIOn()    # if you don't want to play against AI, make this line a comment
    """ Attention !!!!!
        need to check what  the AI is doning if the user only insert arrows,
        is it start moving at some point """
    # board.printBoard()
    # board.insertArrow('R1', Directions.Up)
    # board.insertArrow('G1', Directions.Down)
    # board.insertArrow('R2', Directions.Down)
    # board.insertArrow('G2', Directions.DownLeft)
    # board.move('R1', (4, 1))
    # board.printBoard()
    # board.move('G2', (2, 1))
    # board.printBoard()
    # board.insertArrow('R2', Directions.Up)
    # board.move('G1', (3, 1))
    # board.move('R2', (2, 1))
    # board.printBoard()
    # board.insertArrow("G1", Directions.Down)
    # board.insertArrow('R1', Directions.UpLeft)

    # jsonBoard = board.boardToJson()
    # #print(jsonBoard)
    # board.jsonToBoard(jsonBoard)
    #
    # board.move('G2', (3, 0))
    # jsonBoard = board.boardToJson()
    # #print(jsonBoard)
    # board.jsonToBoard(jsonBoard)

    #print(AI.alphaBetaSearch(board.boardToJson()))
    sys.exit(app.exec_())









