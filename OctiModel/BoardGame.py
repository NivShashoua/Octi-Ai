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

    """ return a list of all the octs """
    def listOfAllOct(self):
        return [self.__green1, self.__green2, self.__green3, self.__green4,
                self.__red1, self.__red2, self.__red3, self.__red4]

    """ Change the turn of the player """
    def __changeTurn(self):
        if self.__turn == Players.Green:
            self.__turn = Players.Red
        else:
            self.__turn = Players.Green

    """ Insert an arrow in your turn """
    def insertArrow(self, oct, arrow):
        if self.__turn == Players.Green:
            if oct == 'G1':
                if not self.__green1.insertArrow(arrow):
                    return  # if there is already an arrow inside
            elif oct == 'G2':
                if not self.__green2.insertArrow(arrow):
                    return
            elif oct == 'G3':
                if not self.__green3.insertArrow(arrow):
                    return
            elif oct == 'G4':
                if not self.__green4.insertArrow(arrow):
                    return
            else:
                return  # if the oct symbol was illegal, do nothing

        elif self.__turn == Players.Red:
            if oct == 'R1':
                if not self.__red1.insertArrow(arrow):
                    return   # if there is already an arrow inside
            elif oct == 'R2':
                if not self.__red2.insertArrow(arrow):
                    return
            elif oct == 'R3':
                if not self.__red3.insertArrow(arrow):
                    return
            elif oct == 'R4':
                if not self.__red4.insertArrow(arrow):
                    return
            else:
                return  # if the oct symbol was illegal, do nothing

        # decrease one arrow to the player who used it
        if self.__turn == Players.Green:
            self.__greenArrows = self.__greenArrows - 1
        else:
            self.__redArrows = self.__redArrows - 1

        self.__changeTurn() # change the turn

    """ return the coordinates of the oct """
    def whereIs(self, oct):
        if oct == 'G1':
            self.__green1.getPlace()
        elif oct == 'G2':
            self.__green2.getPlace()
        elif oct == 'G3':
            self.__green3.getPlace()
        elif oct == 'G4':
            self.__green4.getPlace()
        elif oct == 'R1':
            self.__red1.getPlace()
        elif oct == 'R2':
            self.__red2.getPlace()
        elif oct == 'R3':
            self.__red3.getPlace()
        elif oct == 'R4':
            self.__red4.getPlace()

    """ What is the possible movement for an oct """
    def whereToGo(self, oct):
        # TODO: complete the function
        arrows = []     # list of all the arrows in the wanted oct
        if self.__turn == Players.Green:
            if oct == 'G1':
                octObj = self.__green1
                arrows = self.__green1.showAllArrows()
            elif oct == 'G2':
                octObj = self.__green2
                arrows = self.__green2.showAllArrows()
            elif oct == 'G3':
                octObj = self.__green3
                arrows = self.__green3.showAllArrows()
            elif oct == 'G4':
                octObj = self.__green4
                arrows = self.__green4.showAllArrows()
            else:
                return  # if the oct symbol was illegal, do nothing

        elif self.__turn == Players.Red:
            if oct == 'R1':
                octObj = self.__red1
                arrows = self.__red1.showAllArrows()
            elif oct == 'R2':
                octObj = self.__red2
                arrows = self.__red2.showAllArrows()
            elif oct == 'R3':
                octObj = self.__red3
                arrows = self.__red3.showAllArrows()
            elif oct == 'R4':
                octObj = self.__red4
                arrows = self.__red4.showAllArrows()
            else:
                return  # if the oct symbol was illegal, do nothing

        print("\narrows- ", arrows)

    """ move an oct """
    def move(self, player, oct, direction):
        # TODO: complete the function
        if not isinstance(direction, Directions):
            raise TypeError('direction must be an instance of Directions Enum')

        if not isinstance(player, Players):
            raise TypeError('player must be an instance of Players Enum')

        if not isinstance(oct, Oct):
            raise TypeError('oct must be an instance of Oct class')

    """ print the current state of the board """
    def printBoard(self):
        print('', end=' ')
        allOctList = self.listOfAllOct()
        for row in range(self.__BOARD_LENGTH):
            for col in range(self.__BOARD_WIDTH):
                inLocation = '--'   # what is inside this location
                for oct in allOctList:
                    if (row, col) == oct.getPlace():
                        inLocation = oct.getName()
                        break
                print(inLocation, end=' ')
            print("\n", end=' ')
