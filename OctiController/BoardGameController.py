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
    def __init__(self, model, view, AI):
        #app = QApplication(sys.argv)

        self.__board = model
        self.__view = view

        # remember the chosen oct before the insert arrow window pops. exist so the player can't cheat
        self.__chosenOctInsertArrow = None

        # when clicking the insert button run the insertArrow function (connect between the button and this function)
        self.__view.connectFunctionToInsertButton(self.insertArrow)

        # when clicking on any button in the insert arrow function window, run the function arrowButton
        self.__view.connectFunctionToAllButtons(self.arrowButton)

        # when clicking the on the mouse run the musePressAction function
        # (connect between the mouse press and this function)
        self.__view.connectFunctionToMousePress(self.mousePressAction)

        ##################
        # AI Parameters: #
        ##################
        self.__platAgainstAI = False
        self.__AI = AI


        #sys.exit(app.exec_())

    """" pop the windows to insert an arrow, when cilcked the insert an arrow button """
    def insertArrow(self):
        self.__chosenOctInsertArrow = self.__view.getChosenOct()    # the name of the chosen oct
        if self.__chosenOctInsertArrow is None:
            self.__view.showMassage("you have to click on the oct you want to insert arrows first.")
        else:
            self.__view.showInsertArrowWindow()

    """ when clicking on a button in the insert arrow window,
        insert an arrow to the oct according to the pushed button """
    def arrowButton(self):
        buttonText = self.__view.sender().text()
        oct = self.__chosenOctInsertArrow
        succeeded = False   # if the arrow insert succeeded turn it to True, else it will remain False

        if buttonText == "Up":
            succeeded = self.__board.insertArrow(oct, Directions.Up)

        elif buttonText == "Up Right":
            succeeded = self.__board.insertArrow(oct, Directions.UpRight)

        elif buttonText == "Right":
            succeeded = self.__board.insertArrow(oct, Directions.Right)

        elif buttonText == "Down Right":
            succeeded = self.__board.insertArrow(oct, Directions.DownRight)

        elif buttonText == "Down":
            succeeded = self.__board.insertArrow(oct, Directions.Down)

        elif buttonText == "Down Left":
            succeeded = self.__board.insertArrow(oct, Directions.DownLeft)

        elif buttonText == "Left":
            succeeded = self.__board.insertArrow(oct, Directions.Left)

        elif buttonText == "Up Left":
            succeeded = self.__board.insertArrow(oct, Directions.UpLeft)

        if succeeded:
            self.__view.closeInsertArrowWindow()    # close the insert arrow window
            self.__view.repaint()

            # if the AI is on and its his turn (he is always the green player).
            if self.__platAgainstAI and self.__board.whoseTurn() == Players.Green:
                self.__handleAI()

        else:
            self.__view.showMassage("this arrow already inside this oct")

    """ if the mouse pressed on an oct show where it can go """
    def mousePressAction(self, event):
        matrixRow = (event.y() - Y_START) // SQUARE_SIZE
        matrixCol = (event.x() - X_START) // SQUARE_SIZE

        # if you pressed out of bound, changed the coordinates to be (-1, -1)
        if matrixRow >= NUMBER_OF_ROW or matrixRow < 0 or matrixCol >= NUMBER_OF_COL or matrixCol < 0:
            matrixRow = -1
            matrixCol = -1

        coordinates = (matrixRow, matrixCol)

        # if the user already clicked on an oct he can move it (only to legal movement area)
        if self.__view.getChosenOct() is not None:
            possibleEatenOcts = self.__board.move(self.__view.getChosenOct(), coordinates)
            if possibleEatenOcts is not None:
                self.__view.clickedOct(None)
                self.__view.repaint()

                # ask the user if he want to eat the octs
                self.__handleQuestionBox(possibleEatenOcts)

                # check if some player won
                winner = self.__board.isGoalState()
                if winner == Players.Green:
                    self.__view.showMassage("The Green Player Won!!!")
                elif winner == Players.Red:
                    self.__view.showMassage("The Red Player Won!!!")
                return

        # get the name of the oct that the user clicked on, if he clicked on it
        octName = self.__board.getOctNameFromCordinates(coordinates)
        # remember the name of the oct that had been click on( or None if the user didn't click in an oct)
        self.__view.clickedOct(octName)
        # paint in white all the possible moves for the chosen oct
        self.__view.repaint()

        # if the AI is on and its his turn (he is always the green player).
        if self.__platAgainstAI and self.__board.whoseTurn() == Players.Green:
            self.__handleAI()

    """ pop a question box that ask the user if he want to eat a certain oct """
    def __handleQuestionBox(self, allEatenOct):
        for oct in allEatenOct:
            buttonReply = self.__view.showQuestionBox("Do you want to eat the oct: " + oct + " ?")
            if buttonReply == QMessageBox.Yes:
                self.__board.kill(oct)

    """ when you use this function you will play against th computer """
    def playAgainstAIOn(self):
        self.__platAgainstAI = True

    """ let the AI plays his turn """
    def __handleAI(self):
        self.__view.clickedOct(None)
        currentState = self.__board.boardToJson()
        nextState = self.__AI.alphaBetaSearch(currentState)
        self.__board.jsonToBoard(nextState)
        self.__view.repaint()
