import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from OctiModel.Enums import *
import OctiModel.BoardGame
from OctiView.BoardGameView import BoardGameView

class BoardGameController():

    """ Constuctor """
    def __init__(self, model, view):
        #app = QApplication(sys.argv)
        self.__board = model
        self.__view = view
        self.__insertButton = self.__view.insertButton()
        self.__insertButton.clicked.connect(self.insertArrow)
        #sys.exit(app.exec_())

    def insertArrow(self):
        print("LOL")
