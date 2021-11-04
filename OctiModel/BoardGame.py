from .Oct import *
from .Enums import *
import json

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

        # the current state of the board as string (for the AI)
        self.__currentStateString = ""

    """ list of all the oct """
    def __listOfAllOct(self):
        return [self.__green1, self.__green2, self.__green3, self.__green4,
                self.__red1, self.__red2, self.__red3, self.__red4]

    """ return a list of all the octs that are alive"""
    def __listOfAllOctAlive(self):
        allAliveOct = []
        for oct in self.__listOfAllOct():
            # if the oct is alive get him inside the list
            if oct.isAlive():
                allAliveOct.append(oct)
        return allAliveOct

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

    """ Insert an arrow in your turn 
        :return True if the insert succeeded, and false if there is an arrow already inside"""
    def insertArrow(self, oct, arrow):
        octObj = self.__octObject(oct)
        if octObj in self.__listOfAllOctAlive() and octObj.getPlayer() == self.__turn and self.__playerArrowsNotEmpty():
            if not octObj.insertArrow(arrow):
                return False    # if there is already an arrow inside
        else:
            return False  # if the oct symbol was illegal or its not the player turn, do nothing

        # decrease one arrow to the player who used it
        if self.__turn == Players.Green:
            self.__greenArrows = self.__greenArrows - 1
        else:
            self.__redArrows = self.__redArrows - 1

        self.__changeTurn()     # change the turn
        return True

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
        row, col = location

        if direction == Directions.Up:
            if row == 0:
                return self.__LocationError
            row = row - 1

        elif direction == Directions.UpRight:
            if row == 0 or col == self.__BOARD_WIDTH - 1:
                return self.__LocationError
            row = row - 1
            col = col + 1

        elif direction == Directions.Right:
            if col == self.__BOARD_WIDTH - 1:
                return self.__LocationError
            col = col + 1

        elif direction == Directions.DownRight:
            if row == self.__BOARD_LENGTH - 1 or col == self.__BOARD_WIDTH - 1:
                return self.__LocationError
            row = row + 1
            col = col + 1

        elif direction == Directions.Down:
            if row == self.__BOARD_LENGTH - 1:
                return self.__LocationError
            row = row + 1

        elif direction == Directions.DownLeft:
            if row == self.__BOARD_LENGTH - 1 or col == 0:
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
        if the place is occupied return the name of the oct that is there, if not return None. """
    def __isOccupied(self, location):
        for oct in self.__listOfAllOctAlive():
            if oct.getPlace() == location:
                return oct.getName()
        return None

    """ update the 'possibleJumpsAndEatenOct' list with all the locations the oct can move after
        the jump( can be multiple jump), and the list of all the octs it can eat """
    def __handelJump(self, location, arrows, possibleJumpsAndEatenOct, eatenOcts):
        # the stop condition is check if there wasn't a change in the list possibleJumps
        if location != self.__LocationError and self.__isOccupied(location) is None\
                and location not in possibleJumpsAndEatenOct:
            possibleJumpsAndEatenOct[location] = eatenOcts  # add the new possible location with the possible eaten octs
            for direction in arrows:
                newLocation = self.__getCoordinate(location, direction)
                # you can do multiple jumps only if there are other octs next to it
                if newLocation != self.__LocationError and self.__isOccupied(newLocation) is not None:
                    # create a new eaten oct list that have the old eaten octs plus the new one
                    newEatenOct = eatenOcts + [self.__isOccupied(newLocation)]
                    newJumpLocation = self.__getCoordinate(newLocation, direction)
                    self.__handelJump(newJumpLocation, arrows, possibleJumpsAndEatenOct, newEatenOct)

    """ What are all the possible movement for an oct, and the possible eaten octs.
        parameter - String of the oct name. return - dictionary of the possible moves, and the octs it eat """
    def whereToGo(self, oct):
        # a dictionary that the key is the location of the possible moves and the values are the eaten octs
        possibleMovesAndEatenOct = {}
        octObj = self.__octObject(oct)
        location = octObj.getPlace()

        # check if the oct is alive
        if octObj in self.__listOfAllOctAlive():
            arrows = octObj.showAllArrows()
        else:
            return  # if the oct symbol was illegal or the oct is already dead, do nothing

        for direction in arrows:
            newLocation = self.__getCoordinate(location, direction)
            if newLocation != self.__LocationError:
                # if the near location is not occupied, add it to the dictionary: possibleMovesAndEatenOct,
                # with empty list of eaten octs
                if self.__isOccupied(newLocation) is None:
                    possibleMovesAndEatenOct[newLocation] = []

                # if there might be a jump
                else:
                    # list of all the possible eaten octs
                    eatenOcts = [self.__isOccupied(newLocation)]
                    # enter the name of the oct that occupied the area
                    jumpLocation = self.__getCoordinate(newLocation, direction)
                    self.__handelJump(jumpLocation, arrows, possibleMovesAndEatenOct, eatenOcts)

        return possibleMovesAndEatenOct

    """ move an oct to a specific coordinate
        if the move succeed return True, else return False"""
    def move(self, oct, coordinate):
        possibleMovesAndEatenOct = self.whereToGo(oct)
        # check if its a legal move for this oct.
        if coordinate in possibleMovesAndEatenOct.keys():
            octObj = self.__octObject(oct)
            # check that the player that trying to move the oct is its owner.
            if octObj.getPlayer() == self.__turn:
                octObj.setPlace(coordinate)
                self.__changeTurn()     # change the turn
                return possibleMovesAndEatenOct.get(coordinate)
        return None

    """ according to the place in the board the function return the name of the oct that is there, if its really there,
    else return None """
    def getOctNameFromCordinates(self, coordinates):
        for oct in self.__listOfAllOctAlive():
            if oct.getPlace() == coordinates:
                return oct.getName()

        return None

    """ :return the player who one (Players.green or Players.red). if no one one return None """
    def isGoalState(self):

        greenGoalCoordinates = [(5, 1), (5, 2), (5, 3), (5, 4)]
        AllGreenOctDead = True
        redGoalCoordinates = [(1, 1), (1, 2), (1, 3), (1, 4)]
        AllRedOctDead = True
        for oct in self.__listOfAllOctAlive():
            if oct.getPlayer() == Players.Green:
                AllGreenOctDead = False     # the green player still in the game, not dead yet

                # if one oct from the green got to the goal coordinates
                if oct.getPlace() in greenGoalCoordinates:
                    return Players.Green

            elif oct.getPlayer() == Players.Red:
                AllRedOctDead = False       # the red player still in the game, not dead yet

                # if one oct from the red got to the goal coordinates
                if oct.getPlace() in redGoalCoordinates:
                    return Players.Red
        # all the green oct are dead, red won
        if AllGreenOctDead:
            return Players.Red
        # all the red oct are dead, green won
        if AllRedOctDead:
            return Players.Green

        return None     # no one won

    """ kill/eat this oct """
    def kill(self, oct):
        self.__octObject(oct).death()

    """ return how many arrows left for the player given by the parameter """
    def arrowsLeft(self, player):
        if player == Players.Green:
            return str(self.__greenArrows)
        elif player == Players.Red:
            return str(self.__redArrows)

    """ return the player that need to play now """
    def whoseTurn(self):
        if self.__turn == Players.Green:
            return "Green"
        else:
            return "Red"

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

    """"""""""""""""" FUNCTIONS FOR THE AI """""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""

    def setCurrentState(self, str):
        self.__currentStateString = str

    def getCurrentState(self):
        return self.__currentStateString

    def jsonToBoard(self, jsonBoard):
        board = json.loads(jsonBoard)
        print(type(board))
    # loads - take a json, make an object.
    # dumps - take a string, make a json
    # >>> hostname = "machineA.host.com"
    # >>> data = {'Machine Name': hostname}
    # >>> json.dumps(data)
    # '{"Machine Name": "machineA.host.com"}'

    def boardToJson(self):
        jsonBoard = {
            'Turn': self.whoseTurn(),
            'Green Arrows': self.__greenArrows,
            'Red Arrows': self.__redArrows,

            'G1Alive?': self.__green1.isAlive(),
            'G1 Coordinate': self.__green1.getPlace(),
            'G1 Arrows': self.__green1.showAllArrows(),

            'G2Alive?': self.__green2.isAlive(),
            'G2 Coordinate': self.__green2.getPlace(),
            'G2 Arrows': self.__green2.showAllArrows(),

            'G3Alive?': self.__green3.isAlive(),
            'G3 Coordinate': self.__green3.getPlace(),
            'G3 Arrows': self.__green3.showAllArrows(),

            'G4Alive?': self.__green4.isAlive(),
            'G4 Coordinate': self.__green4.getPlace(),
            'G4 Arrows': self.__green4.showAllArrows(),

            'R1Alive?': self.__red1.isAlive(),
            'R1 Coordinate': self.__red1.getPlace(),
            'R1 Arrows': self.__red1.showAllArrows(),

            'R2Alive?': self.__red2.isAlive(),
            'R2 Coordinate': self.__red2.getPlace(),
            'R2 Arrows': self.__red2.showAllArrows(),

            'R3Alive?': self.__red3.isAlive(),
            'R3 Coordinate': self.__red3.getPlace(),
            'R3 Arrows': self.__red3.showAllArrows(),

            'R4Alive?': self.__red4.isAlive(),
            'R4 Coordinate': self.__red4.getPlace(),
            'R4 Arrows': self.__red4.showAllArrows()
                    }
        return json.dumps(jsonBoard)

    """ return a list of all the successors of this specific state (return them as json). """
    def getSuccessors(self):
        """TODO: together"""

    """ return a list of names of all the alive oct of a specific player. """
    def listOfAllPlayerAliveOct(self, player):
        playerAliveOct = []
        for oct in self.__listOfAllOctAlive():
            if oct.getPlayer() == player:
                playerAliveOct.append(oct.getName())
        return playerAliveOct

    """ return a list of all the arrows of a given oct.
        the parameter is the oct's name. """
    def allArrows(self, oct):
        return self.__octObject(oct).showAllArrows()

    """ return the number of steps of the shortest path from the given oct to the gaol. """
    def manhattanStepsToGoal(self, oct):
        """ TODO: niv """