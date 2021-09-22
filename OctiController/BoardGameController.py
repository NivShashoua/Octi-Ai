import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from OctiModel.Enums import *
import OctiModel.BoardGame
import OctiView.BoardGameView

class BoardGameController():

    """ Constuctor """
    def __init__(self, model, view):
        #app = QApplication(sys.argv)
        self.__board = model
        self.__view = view
        self.__view.connectFunctionToInsertButton(self.insertArrow)
        #sys.exit(app.exec_())


    """" pop the windows to insert an arrow, when cilcked the insert an arrow button """
    def insertArrow(self):
        self.__view.showMassage("NANIII")
