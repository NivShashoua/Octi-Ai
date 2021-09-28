import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from OctiModel.Enums import *
import OctiModel.BoardGame
import OctiView.BoardGameView
from OctiView.ConstantView import *

class BoardGameController():

    """ Constuctor """
    def __init__(self, model, view):
        #app = QApplication(sys.argv)

        self.__board = model
        self.__view = view

        # when clicking the insert button run the insertArrow function (connect between the button and this function)
        self.__view.connectFunctionToInsertButton(self.insertArrow)

        # when clicking the on the mouse run the musePressAction function
        # (connect between the mouse press and this function)
        self.__view.connectFunctionToMousePress(self.mousePressAction)

        #sys.exit(app.exec_())

    """" pop the windows to insert an arrow, when cilcked the insert an arrow button """
    def insertArrow(self):
        self.__view.showMassage("NANIII")

    def mousePressAction(self, event):
        x = event.x()
        y = event.y()
        matrixRow = (y - Y_START) // SQUARE_SIZE
        matrixCol = (x - X_START) // SQUARE_SIZE

        if matrixRow >= NUMBER_OF_ROW or matrixRow < 0 or matrixCol >= NUMBER_OF_COL or matrixCol < 0:
            matrixRow = -1
            matrixCol = -1

        coordinates = (matrixRow, matrixCol)
        octName = self.__board.getOctNameFromCordinates(coordinates)
        print("(", matrixRow, ",", matrixCol, ")")
        print(octName)
