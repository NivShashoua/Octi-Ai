from .Oct import *
from .Enums import *


class BoardGame:

    """Constant"""
    __BOARD_LENGTH = 7
    __BOARD_WIDTH = 6

    """Constructor"""
    def __init__(self):
        # which player turn
        self.__turn = Players.Green

        # all the oct on the game
        self.__green1 = Oct(Players.Green, "G1", 1, 1)
        self.__green2 = Oct(Players.Green, "G2", 1, 2)
        self.__green3 = Oct(Players.Green, "G3", 1, 3)
        self.__green4 = Oct(Players.Green, "G4", 1, 4)
        self.__red1 = Oct(Players.Red, "R1", 5, 1)
        self.__red2 = Oct(Players.Red, "R2", 5, 2)
        self.__red3 = Oct(Players.Red, "R3", 5, 3)
        self.__red4 = Oct(Players.Red, "R4", 5, 4)

        # number of arrows each players have. initial 12 for each
        self.__greenArrows = 12
        self.__redArrows = 12

    """ list of all the oct """
    def __listOfAllOct(self):
        return [self.__green1, self.__green2, self.__green3, self.__green4,
                self.__red1, self.__red2, self.__red3, self.__red4]

    """ return a list of all the octs that are alive"""
    def __listOfAllOctAlive(self):
        allOct = self.__listOfAllOct()
        for oct in allOct:
            # if the oct is dead get him out of the list
            if not oct.isAlive():
                allOct.remove(oct)
        return allOct

    """ convert oct name to oct object """
    def __octObject(self, oct):
        for octObj in self.__listOfAllOct():
            if octObj.getName() == oct:
                return octObj

    """ Change the turn of the player """
    def __changeTurn(self):
        if self.__turn == Players.Green:
            self.__turn = Players.Red
        else:
            self.__turn = Players.Green

    """ Insert an arrow in your turn """
    def insertArrow(self, oct, arrow):
        octObj = self.__octObject(oct)
        if octObj in self.__listOfAllOctAlive() and octObj.getPlayer() == self.__turn:
            if not octObj.insertArrow(arrow):
                return  # if there is already an arrow inside
        else:
            return   # if the oct symbol was illegal or its not the player turn, do nothing

        # decrease one arrow to the player who used it
        if self.__turn == Players.Green:
            self.__greenArrows = self.__greenArrows - 1
        else:
            self.__redArrows = self.__redArrows - 1

        self.__changeTurn() # change the turn

    """ return the coordinates of the oct """
    def whereIs(self, oct):
        return self.__octObject().getPlace()

    """ What is the possible movement for an oct """
    def whereToGo(self, oct):
        # TODO: complete the function
        octObj = self.__octObject(oct)
        arrows = []     # list of all the arrows in the wanted oct

        # check if the oct is alive an if its the player turn
        if octObj in self.__listOfAllOctAlive() and octObj.getPlayer() == self.__turn:
            arrows = octObj.showAllArrows()
        else:
            return  # if the oct symbol was illegal or it's not the right player, do nothing


        print("\narrows- ", arrows)

    """ move an oct to a specfic cordinates"""
    def move(self, oct, row, col):
        location = (row, col)
        if location in self.whereToGo(oct):
            octObj = self.__octObject(oct)
            octObj.setPlace(location)

    """ print the current state of the board """
    def printBoard(self):
        print('', end=' ')
        allOctList = self.__listOfAllOctAlive()
        for row in range(self.__BOARD_LENGTH):
            for col in range(self.__BOARD_WIDTH):
                inLocation = '--'   # what is inside this location
                for oct in allOctList:
                    if (row, col) == oct.getPlace():
                        inLocation = oct.getName()
                        break
                print(inLocation, end=' ')
            print("\n", end=' ')
