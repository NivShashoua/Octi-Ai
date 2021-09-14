import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .CellView import *
import OctiModel.BoardGame
from OctiModel.Enums import *


class BoardGameView(QMainWindow):

    """ Constants """
    __WINDOW_LENGTH = 900
    __WINDOW_WIDTH = 900
    __SQUARE_SIZE = 125

    __NUMBER_OF_ROW = 7
    __NUMBER_OF_COL = 6

    __X_START = (__WINDOW_WIDTH - __SQUARE_SIZE * __NUMBER_OF_COL) // 2
    __Y_START = (__WINDOW_LENGTH - __SQUARE_SIZE * __NUMBER_OF_ROW) // 2

    """ Constructor """
    def __init__(self, model):
        app = QApplication(sys.argv)
        super().__init__()
        self.setWindowTitle("Octi")
        self.setGeometry(300, 100, self.__WINDOW_WIDTH, self.__WINDOW_LENGTH)

        self.show()
        sys.exit(app.exec_())

    """Override. draw the board"""
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.black))
        self.__paintBoard(qp)


        qp.end()

    def __paintBoard(self, qp):
        qp.setPen(QColor(Qt.black))

        for row in range(self.__NUMBER_OF_ROW):
            for col in range(self.__NUMBER_OF_COL):
                # paint the base of the green player in green
                if row == 1 and col != 0 and col != self.__NUMBER_OF_COL - 1:
                    qp.fillRect(col * self.__SQUARE_SIZE + self.__X_START, row * self.__SQUARE_SIZE + self.__Y_START,
                                self.__SQUARE_SIZE, self.__SQUARE_SIZE, QBrush(Qt.green))
                # paint the base of the red player in red
                elif row == self.__NUMBER_OF_ROW - 2 and col != 0 and col != self.__NUMBER_OF_COL - 1:
                    qp.fillRect(col * self.__SQUARE_SIZE + self.__X_START, row * self.__SQUARE_SIZE + self.__Y_START,
                                self.__SQUARE_SIZE, self.__SQUARE_SIZE, QBrush(Qt.red))
                # paint all the regular square in light gray
                else:
                    qp.fillRect(col * self.__SQUARE_SIZE + self.__X_START, row * self.__SQUARE_SIZE + self.__Y_START,
                                self.__SQUARE_SIZE, self.__SQUARE_SIZE, QBrush(Qt.lightGray))

                qp.drawRect(col * self.__SQUARE_SIZE + self.__X_START, row * self.__SQUARE_SIZE + self.__Y_START,
                            self.__SQUARE_SIZE, self.__SQUARE_SIZE)

    def __paintOcts(self, qp):
        """TODO: complete the function"""

    def __showMassage(self, str):
        """TODO: complete the function"""
