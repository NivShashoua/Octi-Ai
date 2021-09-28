from .Oct import *
from .Enums import *


class BoardGame:

    """Constant"""
    __BOARD_LENGTH = 7
    __BOARD_WIDTH = 6
    __LocationError = (-1, -1)

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

    """ return True if the player still have some arrows left, else return False """
    def __playerArrowsNotEmpty(self):
        if self.__turn == Players.Green:
            if self.__greenArrows > 0:
                return True
        else:
            if self.__redArrows > 0:
                return True
        return False

    """ Insert an arrow in your turn """
    def insertArrow(self, oct, arrow):
        octObj = self.__octObject(oct)
        if octObj in self.__listOfAllOctAlive() and octObj.getPlayer() == self.__turn and self.__playerArrowsNotEmpty():
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

    """ given an oct name the function return a list of all the arrows it have """
    def showAllArrows(self, oct):
        octObj = self.__octObject(oct)
        return octObj.showAllArrows()

    """ for all the octs that are alive return this tuple: (name, color, coordinates) """
    def getAllAliveOctInfo(self):
        listOfAllOctPlaces = []
        for oct in self.__listOfAllOctAlive():
            listOfAllOctPlaces.append((oct.getName(), oct.getPlayer(), oct.getPlace()))

        return listOfAllOctPlaces

    """ get the coordinates near the wanted location, according to the direction. 
        if the new location is out of bound then return (-1, -1) """
    def __getCoordinate(self, location, direction):
        row = location[0]
        col = location[1]

        if direction == Directions.Up:
            if row == 0:
                return self.__LocationError
            row = row - 1

        elif direction == Directions.UpRight:
            if row == 0 or col == self.__BOARD_WIDTH:
                return self.__LocationError
            row = row - 1
            col = col + 1

        elif direction == Directions.Right:
            if col == self.__BOARD_WIDTH:
                return self.__LocationError
            col = col + 1

        elif direction == Directions.DownRight:
            if row == self.__BOARD_LENGTH or col == self.__BOARD_WIDTH:
                return self.__LocationError
            row = row + 1
            col = col + 1

        elif direction == Directions.Down:
            if row == self.__BOARD_LENGTH:
                return self.__LocationError
            row = row + 1

        elif direction == Directions.DownLeft:
            if row == self.__BOARD_LENGTH or col == 0:
                return self.__LocationError
            row = row + 1
            col = col - 1

        elif direction == Directions.Left:
            if col == 0:
                return self.__LocationError
            col = col - 1

        elif direction == Directions.UpLeft:
            if row == 0 or col == 0:
                return self.__LocationError
            row = row - 1
            col = col - 1

        newLocation = (row, col)
        return newLocation

    """ check the location is not occupied by other alive oct. 
        if the place is occupied return true, if not false. """
    def __isOccupied(self, location):
        for oct in self.__listOfAllOctAlive():
            if oct.getPlace() == location:
                return True
        return False

    """ return a list of all the locations the oct can move after the jump( can be multiple jump) """
    def __handelJump(self, location, arrows, possibleJumps):
        # the stop condition is check if there wasn't a change in the list possibleJumps
        if location != self.__LocationError and not self.__isOccupied(location) and location not in possibleJumps:
            possibleJumps.append(location)
            for direction in arrows:
                newLocation = self.__getCoordinate(location, direction)
                # you can do multiple jumps only if there are other octs next to it
                if newLocation != self.__LocationError and self.__isOccupied(newLocation):
                    newJumpLocation = self.__getCoordinate(newLocation, direction)
                    self.__handelJump(newJumpLocation, arrows, possibleJumps)

        return possibleJumps

    """ What are all the possible movement for an oct """
    def whereToGo(self, oct):
        possibleMoves = []
        octObj = self.__octObject(oct)
        location = octObj.getPlace()

        # check if the oct is alive
        if octObj in self.__listOfAllOctAlive():
            arrows = octObj.showAllArrows()
        else:
            return  # if the oct symbol was illegal or it's not the right player, do nothing

        for direction in arrows:
            newLocation = self.__getCoordinate(location, direction)
            if newLocation != self.__LocationError:
                # if the near location is not occupied, add it to the list: possibleMoves
                if not self.__isOccupied(newLocation):
                    possibleMoves.append(newLocation)

                # if there might be a jump
                else:
                    jumpLocation = self.__getCoordinate(newLocation, direction)
                    possibleMoves = possibleMoves + self.__handelJump(jumpLocation, arrows, [])

        return possibleMoves

    """ move an oct to a specific coordinates"""
    def move(self, oct, row, col):
        location = (row, col)
        # check if its a legal move for this oct.
        if location in self.whereToGo(oct):
            octObj = self.__octObject(oct)
            # check that the player that trying to move the oct is its owner.
            if octObj.getPlayer() == self.__turn:
                octObj.setPlace(location)
                self.__changeTurn() # change the turn

    """ according to the place in the board the function return the name of the oct that is there, if its really there,
    else return None """
    def getOctNameFromCordinates(self, coordinates):
        for oct in self.__listOfAllOctAlive():
            if oct.getPlace() == coordinates:
                return oct.getName()

        return None

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
        print("turn:", self.__turn)
        print('\n')

