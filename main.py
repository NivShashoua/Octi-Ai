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
    sys.exit(app.exec_())









