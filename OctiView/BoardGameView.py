import sys
import pathlib
import OctiModel.BoardGame
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from OctiModel.Enums import *
from OctiView.ConstantView import *

class BoardGameView(QMainWindow):

    """ Private Constants """
    # get the full path of the current project location
    __PATH = str(pathlib.Path().absolute()) + "\OctiView\Pictures\\"

    """ Constructor """
    def __init__(self, model):

        super().__init__()

        self.__board = model    # the board game logic object
        # this variable need to get a pointer to mousePressAction function from the class OctiController
        self.mousePressFunction = None
        self.__chosenOct = None  # if the player clicked on an oct, save its name

        self.setWindowTitle("Octi")
        self.setGeometry(300, 100, WINDOW_WIDTH, WINDOW_LENGTH)

        # create a button to insert arrows
        self.__insertArrowButton = QPushButton(self)
        self.__insertArrowButton.setText("Inset Arrow")
        self.__insertArrowButton.setGeometry(INSERT_ARROW_BUTTON_X,
                                             INSERT_ARROW_BUTTON_Y,
                                             INSERT_ARROW_BUTTON_WIDTH,
                                             INSERT_ARROW_BUTTON_LENGTH)
        self.show()

    """Override. draw the board game"""
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.__paintBoard(qp)
        self.__paintOcts(qp)
        self.__colorWhiteSquares(qp)

        qp.end()

    """ paint the board """
    def __paintBoard(self, qp):
        qp.setPen(QColor(Qt.black))

        for row in range(NUMBER_OF_ROW):
            for col in range(NUMBER_OF_COL):
                # paint the base of the green player in green
                if row == 1 and col != 0 and col != NUMBER_OF_COL - 1:
                    qp.fillRect(col * SQUARE_SIZE + X_START, row * SQUARE_SIZE + Y_START,
                                SQUARE_SIZE, SQUARE_SIZE, QBrush(Qt.green))
                # paint the base of the red player in red
                elif row == NUMBER_OF_ROW - 2 and col != 0 and col != NUMBER_OF_COL - 1:
                    qp.fillRect(col * SQUARE_SIZE + X_START, row * SQUARE_SIZE + Y_START,
                                SQUARE_SIZE, SQUARE_SIZE, QBrush(Qt.red))
                # paint all the regular square in light gray
                else:
                    qp.fillRect(col * SQUARE_SIZE + X_START, row * SQUARE_SIZE + Y_START,
                                SQUARE_SIZE, SQUARE_SIZE, QBrush(Qt.lightGray))

                qp.drawRect(col * SQUARE_SIZE + X_START, row * SQUARE_SIZE + Y_START,
                            SQUARE_SIZE, SQUARE_SIZE)

    """ paint all the pieces on the board and all their arrows """
    def __paintOcts(self, qp):

        for octInfo in self.__board.getAllAliveOctInfo():
            octName = octInfo[0]
            octColor = octInfo[1]
            oct_X = octInfo[2][1] * SQUARE_SIZE + X_START   # the oct X coordinate in the view
            oct_Y = octInfo[2][0] * SQUARE_SIZE + Y_START  # the oct Y coordinate in the view

            # get the right pic for the oct according to the color
            if octColor == Players.Green:
                pic = QPixmap(self.__PATH + "Green_Octagon.png")

            else:
                pic = QPixmap(self.__PATH + "Red_Octagon.png")
            # draw the oct
            qp.drawPixmap(oct_X, oct_Y, SQUARE_SIZE, SQUARE_SIZE, pic)
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

            qp.drawPixmap(X, Y, SQUARE_SIZE, SQUARE_SIZE, arrowPic)

    """ pop an massage on the screen,
     with the massage that given as parameter """
    def showMassage(self, str):
        msg = QMessageBox()
        msg.setText(str)
        msg.exec_()

    """ connect a function to the insert arrow button """
    def connectFunctionToInsertButton(self, func):
        self.__insertArrowButton.clicked.connect(func)

    """ put the pointer of the function "mousePressAction" in the class 
    OctiController in the variable mousePressFunction  """
    def connectFunctionToMousePress(self, func):
        self.mousePressFunction = func

    """Override. when the mouse is press run the function "mousePressAction" in the class OctiController"""
    def mousePressEvent(self, event):
        self.mousePressFunction(event)

    """ paint a chosen square in white """
    def clickedOct(self, octName):
        self.__chosenOct = octName

    """ color the possible moves of the chosen oct(the one that the user clicked on) """
    def __colorWhiteSquares(self, qp):
        # if the player didn't choose his oct
        if self.__chosenOct is None:
            return

        for row, col in self.__board.whereToGo(self.__chosenOct):
            qp.fillRect(col * SQUARE_SIZE + X_START,
                        row * SQUARE_SIZE + Y_START,
                        SQUARE_SIZE, SQUARE_SIZE, QBrush(Qt.white))
            qp.setPen(QColor(Qt.black))
            qp.drawRect(col * SQUARE_SIZE + X_START,
                        row * SQUARE_SIZE + Y_START,
                        SQUARE_SIZE, SQUARE_SIZE)

    """ return the name of the chosen oct. if the user didn't choose an oct return None """
    def getChosenOct(self):
        return self.__chosenOct