from .Enums import *

class Oct:

    """Constructor"""
    def __init__(self, player, name, row, col):
        if not isinstance(player, Players):
            raise TypeError('players must be an instance of Players Enum, Red or Green')
        self.__name = name
        self.__player = player  # the oct belong to player
        self.__isAlive = True   # the oct is alive
        self.__place = (row, col)   # the starting point
        self.__arrowUp = False  # all the arrows and if they are attached to the oct
        self.__arrowUpRight = False
        self.__arrowRight = False
        self.__arrowDownRight = False
        self.__arrowDown = False
        self.__arrowDownLeft = False
        self.__arrowLeft = False
        self.__arrowUpLeft = False

    """ Insert an arrow to an oct, get a parameter of arrowType enum.
        return the true if you succeed to put the arrow inside, else return false """
    def insertArrow(self, arrow):
        if not isinstance(arrow, Directions):
            raise TypeError('arrows must be an instance of Directions Enum')

        if arrow == Directions.Up and not self.__arrowUp:
            self.__arrowUp = True
            return True

        elif arrow == Directions.UpRight and not self.__arrowUpRight:
            self.__arrowUpRight = True
            return True

        elif arrow == Directions.Right and not self.__arrowRight:
            self.__arrowRight = True
            return True

        elif arrow == Directions.DownRight and not self.__arrowDownRight:
            self.__arrowDownRight = True
            return True

        elif arrow == Directions.Down and not self.__arrowDown:
            self.__arrowDown = True
            return True

        elif arrow == Directions.DownLeft and not self.__arrowDownLeft:
            self.__arrowDownLeft = True
            return True

        elif arrow == Directions.Left and not self.__arrowLeft:
            self.__arrowLeft = True
            return True

        elif arrow == Directions.UpLeft and not self.__arrowUpLeft:
            self.__arrowUpLeft = True
            return True

        # fail to insert the arrow
        else:
            return False

    """ Check if the arrow is inside the oct """
    def isArrow(self, arrow):
        if not isinstance(arrow, Directions):
            raise TypeError('arrows must be an instance of Directions Enum')

        if arrow == Directions.Up:
            return self.__arrowUp

        elif arrow == Directions.UpRight:
            return self.__arrowUpRight

        elif arrow == Directions.Right:
            return self.__arrowRight

        elif arrow == Directions.DownRight:
            return self.__arrowDownRight

        elif arrow == Directions.Down:
            return self.__arrowDown

        elif arrow == Directions.DownLeft:
            return self.__arrowDownLeft

        elif arrow == Directions.Left:
            return self.__arrowLeft

        elif arrow == Directions.UpLeft:
            return self.__arrowUpLeft

    """ return a list of all the directions in which there is an arrow that point to this directions"""
    def showAllArrows(self):
        arrows = []
        if self.__arrowUp:
            arrows.append(Directions.Up)
        if self.__arrowUpRight:
            arrows.append(Directions.UpRight)
        if self.__arrowRight:
            arrows.append(Directions.Right)
        if self.__arrowDownRight:
            arrows.append(Directions.DownRight)
        if self.__arrowDown:
            arrows.append(Directions.Down)
        if self.__arrowDownLeft:
            arrows.append(Directions.DownLeft)
        if self.__arrowLeft:
            arrows.append(Directions.Left)
        if self.__arrowUpLeft:
            arrows.append(Directions.UpLeft)
        return arrows

    """ Is the oct alive """
    def isAlive(self):
        return self.__isAlive

    """ The oct died """
    def death(self):
        self.__isAlive = False

    """ return the coordinates of the oct """
    def getPlace(self):
        return self.__place

    """ :return the oct name """
    def getName(self):
        return self.__name
