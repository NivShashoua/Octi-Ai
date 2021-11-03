import enum

""" Types of arrows """
class Directions(str,enum.Enum):
    Up = "Up"
    UpRight = "UpRight"
    Right = "Right"
    DownRight = "DownRight"
    Down = "Down"
    DownLeft = "DownLeft"
    Left = "Left"
    UpLeft = "UpLeft"

class Players(enum.Enum):
    Red = 1
    Green = 2