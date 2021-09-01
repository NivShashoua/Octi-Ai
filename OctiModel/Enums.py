import enum

""" Types of arrows """
class Directions(enum.Enum):
    Up = 1
    UpRight = 2
    Right = 3
    DownRight = 4
    Down = 5
    DownLeft = 6
    Left = 7
    UpLeft = 8

class Players(enum.Enum):
    Red = 1
    Green = 2