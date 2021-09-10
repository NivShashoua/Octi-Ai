import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

import OctiModel.BoardGame
from OctiModel.Enums import *

class BoardGameView(QMainWindow):

    count = 0

    def __init__(self, model):
        app = QApplication(sys.argv)

        super(BoardGameView, self).__init__()

        self.show()
        sys.exit(app.exec_())
