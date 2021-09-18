import sys
import pathlib
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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

    __ARROW_LENGTH = 30
    __ARROW_WIDTH = 8

    """ Constructor """
    def __init__(self, model):
        app = QApplication(sys.argv)
        super().__init__()
        self.__board = model
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
        self.__paintOcts(qp)

        qp.end()

    """ paint the board """
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

    """ paint all the pieces on the board and all their arrows """
    def __paintOcts(self, qp):
        path = str(pathlib.Path().absolute())    # get the full path of the current project location

        for octInfo in self.__board.getAllAliveOctInfo():
            octName = octInfo[0]
            octColor = octInfo[1]
            oct_X = octInfo[2][1] * self.__SQUARE_SIZE + self.__X_START   # the oct X coordinate in the view
            oct_Y = octInfo[2][0]  * self.__SQUARE_SIZE + self.__Y_START  # the oct Y coordinate in the view

            # get the right pic for the oct according to the color
            if octColor == Players.Green:
                pic = QPixmap(path + "\OctiView\Green_Octagon.png")

            else:
                pic = QPixmap(path + "\OctiView\Red_Octagon.png")
            # draw the oct
            qp.drawPixmap(oct_X, oct_Y, self.__SQUARE_SIZE, self.__SQUARE_SIZE , pic)
            # draw all its arrows
            self.__handelArrows(qp, octName, oct_X, oct_Y)

    """ paint the arrows of a specific oct.
        get as parameters: 1. the QPainter, 2. the oct name, 3. the X coordinate, 4. the Y coordinate """
    def __handelArrows(self, qp, oct, X, Y):
        """TODO: complete the function"""
        arrows = self.__board.showAllArrows(oct)
        center_X = X + (self.__SQUARE_SIZE // 2)    # the X coordinate of the center of the square
        center_Y = Y + (self.__SQUARE_SIZE // 2)    # the Y coordinate of the center of the square
        for arrow in arrows:
            angle = 0.0  # need to be double
            arrow_X = center_X
            arrow_Y = center_Y
            if arrow == Directions.Up:
                angle = angle
                arrow_X = center_X - 2
                arrow_Y = center_Y - 50

            elif arrow == Directions.UpRight:
                angle = angle + 45
                arrow_X = center_X + 30
                arrow_Y = center_Y - 30

            elif arrow == Directions.Right:
                angle = angle + 90
                arrow_X = center_X + 30
                arrow_Y = center_Y

            elif arrow == Directions.DownRight:
                angle = angle + 135
                arrow_X = center_X + 30
                arrow_Y = center_Y + 30

            elif arrow == Directions.Down:
                angle = angle + 180
                arrow_X = center_X - 2
                arrow_Y = center_Y + 20

            elif arrow == Directions.DownLeft:
                angle = angle + 225
                arrow_X = center_X - 30
                arrow_Y = center_Y + 30

            elif arrow == Directions.Left:
                angle = angle + 270
                arrow_X = center_X - 30
                arrow_Y = center_Y

            elif arrow == Directions.UpLeft:
                angle = angle + 315
                arrow_X = center_X - 30
                arrow_Y = center_Y - 30

            # qp.translate(arrow_X, arrow_Y)
            # qp.rotate(-10)
            arrowView = QRect(arrow_X, arrow_Y, self.__ARROW_WIDTH, self.__ARROW_LENGTH)
            qp.fillRect(arrowView, QBrush(Qt.red))
            qp.setPen(QColor(Qt.black))
            qp.drawRect(arrow_X, arrow_Y, self.__ARROW_WIDTH, self.__ARROW_LENGTH)
            # qp.translate(0, 0)
            #  qp.rotate(0)


    def __showMassage(self, str):
        """TODO: complete the function"""
