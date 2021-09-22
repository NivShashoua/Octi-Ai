import sys
import pathlib
import OctiModel.BoardGame
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from OctiModel.Enums import *


class BoardGameView(QMainWindow):

    """ Constants """
    __WINDOW_LENGTH = 900
    __WINDOW_WIDTH = 1000
    __SQUARE_SIZE = 125

    __NUMBER_OF_ROW = 7
    __NUMBER_OF_COL = 6

    # the coordinates where the board should be paint in
    __X_START = (__WINDOW_WIDTH - __SQUARE_SIZE * __NUMBER_OF_COL) // 2 - 100
    __Y_START = (__WINDOW_LENGTH - __SQUARE_SIZE * __NUMBER_OF_ROW) // 2

    # all the parameters needed for the Insert Arrow button
    __INSERT_ARROW_BUTTON_LENGTH = 70
    __INSERT_ARROW_BUTTON_WIDTH = 100
    __INSERT_ARROW_BUTTON_X = __X_START + __SQUARE_SIZE * (__NUMBER_OF_COL + 0.5)
    __INSERT_ARROW_BUTTON_Y = __Y_START + __SQUARE_SIZE * (__NUMBER_OF_ROW - 1)

    # get the full path of the current project location
    __PATH = str(pathlib.Path().absolute()) + "\OctiView\Pictures\\"

    """ Constructor """
    def __init__(self, model):

        super().__init__()
        self.__board = model    # the board game logic object
        self.setWindowTitle("Octi")
        self.setGeometry(300, 100, self.__WINDOW_WIDTH, self.__WINDOW_LENGTH)

        # create a button to insert arrows
        self.__insertArrowButton = QPushButton(self)
        self.__insertArrowButton.setText("Inset Arrow")
        self.__insertArrowButton.setGeometry(self.__INSERT_ARROW_BUTTON_X,
                                             self.__INSERT_ARROW_BUTTON_Y,
                                             self.__INSERT_ARROW_BUTTON_WIDTH,
                                             self.__INSERT_ARROW_BUTTON_LENGTH)
        self.show()


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

        for octInfo in self.__board.getAllAliveOctInfo():
            octName = octInfo[0]
            octColor = octInfo[1]
            oct_X = octInfo[2][1] * self.__SQUARE_SIZE + self.__X_START   # the oct X coordinate in the view
            oct_Y = octInfo[2][0]  * self.__SQUARE_SIZE + self.__Y_START  # the oct Y coordinate in the view

            # get the right pic for the oct according to the color
            if octColor == Players.Green:
                pic = QPixmap(self.__PATH + "Green_Octagon.png")

            else:
                pic = QPixmap(self.__PATH + "Red_Octagon.png")
            # draw the oct
            qp.drawPixmap(oct_X, oct_Y, self.__SQUARE_SIZE, self.__SQUARE_SIZE, pic)
            # draw all its arrows
            self.__handelArrows(qp, octName, oct_X, oct_Y)

    """ paint the arrows of a specific oct.
        get as parameters: 1. the QPainter, 2. the oct name, 3. the X coordinate, 4. the Y coordinate """
    def __handelArrows(self, qp, oct, X, Y):
        arrows = self.__board.showAllArrows(oct)

        for arrow in arrows:
            arrowPic = QPixmap()

            if arrow == Directions.Up:
                arrowPic = QPixmap(self.__PATH + "Up.png")

            elif arrow == Directions.UpRight:
                arrowPic = QPixmap(self.__PATH + "UpRight.png")

            elif arrow == Directions.Right:
                arrowPic = QPixmap(self.__PATH + "Right.png")

            elif arrow == Directions.DownRight:
                arrowPic = QPixmap(self.__PATH + "DownRight.png")

            elif arrow == Directions.Down:
                arrowPic = QPixmap(self.__PATH + "Down.png")

            elif arrow == Directions.DownLeft:
                arrowPic = QPixmap(self.__PATH + "DownLeft.png")

            elif arrow == Directions.Left:
                arrowPic = QPixmap(self.__PATH + "DownRight.png")

            elif arrow == Directions.UpLeft:
                arrowPic = QPixmap(self.__PATH + "DownRight.png")

            qp.drawPixmap(X, Y, self.__SQUARE_SIZE, self.__SQUARE_SIZE, arrowPic)

    """ pop an massage on the screen,
     with the massage that given as parameter """
    def showMassage(self, str):
        """TODO: complete the function"""
        msg = QMessageBox()
        msg.setText(str)
        msg.exec_()

    """ connect a function to the insert arrow button """
    def connectFunctionToInsertButton(self, func):
        self.__insertArrowButton.clicked.connect(func)

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        print("(", x, ",", y, ")")

