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
        self.__green1 = Oct(Players.Green)
        self.__green2 = Oct(Players.Green)
        self.__green3 = Oct(Players.Green)
        self.__green4 = Oct(Players.Green)
        self.__red1 = Oct(Players.Red)
        self.__red2 = Oct(Players.Red)
        self.__red3 = Oct(Players.Red)
        self.__red4 = Oct(Players.Red)

        # the initial state of the board
        self.__currentState = {
            (1, 7): 'empty', (2, 7): 'empty', (3, 7): 'empty', (4, 7): 'empty', (5, 7): 'empty', (6, 7): 'empty',
            (1, 6): 'empty', (2, 6): 'G1', (3, 6): 'G2', (4, 6): 'G3', (5, 6): 'G4', (6, 6): 'empty',
            (1, 5): 'empty', (2, 5): 'empty', (3, 5): 'empty', (4, 5): 'empty', (5, 5): 'empty', (6, 5): 'empty',
            (1, 4): 'empty', (2, 4): 'empty', (3, 4): 'empty', (4, 4): 'empty', (5, 4): 'empty', (6, 4): 'empty',
            (1, 3): 'empty', (2, 3): 'empty', (3, 3): 'empty', (4, 3): 'empty', (5, 3): 'empty', (6, 3): 'empty',
            (1, 2): 'empty', (2, 2): 'R1', (3, 2): 'R2', (4, 2): 'R3', (5, 2): 'R4', (6, 2): 'empty',
            (1, 1): 'empty', (2, 1): 'empty', (3, 1): 'empty', (4, 1): 'empty', (5, 1): 'empty', (6, 1): 'empty'
        }

        # the places of all the oct on the board
        self.__octPlaces = {
            'G1': (1, 1),
            'G2': (2, 1),
            'G3': (3, 1),
            'G4': (4, 1),
            'R1': (1, 5),
            'R2': (2, 5),
            'R3': (3, 5),
            'R4': (4, 5)
        }

        # number of arrows each players have. initial 12 for each
        self.__greenArrows = 12
        self.__redArrows = 12

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

        self.__changeTurn() # change the turn

    """ return the coordinates of the oct """
    def whereIs(self, oct):
        return self.__octPlaces[oct]

    """ What is the possible movement for an oct """
    def whereToGo(self, oct):
        # TODO: complete the function
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
        i = 1
        for loc in self.__currentState:
            if i > self.__BOARD_WIDTH:
                print('')
                i = 1
            if self.__currentState.get(loc) == 'empty':
                print('--', end=' ')
            else:
                print(self.__currentState.get(loc), end=' ')
            i = i + 1