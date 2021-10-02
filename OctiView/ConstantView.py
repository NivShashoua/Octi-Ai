import math

WINDOW_X = 300
WINDOW_Y = 100
WINDOW_LENGTH = 900
WINDOW_WIDTH = 1000
SQUARE_SIZE = 125

NUMBER_OF_ROW = 7
NUMBER_OF_COL = 6

# the coordinates where the board should be paint in
X_START = (WINDOW_WIDTH - SQUARE_SIZE * NUMBER_OF_COL) // 2 - 100
Y_START = (WINDOW_LENGTH - SQUARE_SIZE * NUMBER_OF_ROW) // 2

# all the parameters needed for the Insert Arrow button
INSERT_ARROW_BUTTON_LENGTH = 70
INSERT_ARROW_BUTTON_WIDTH = 100
INSERT_ARROW_BUTTON_X = X_START + SQUARE_SIZE * (NUMBER_OF_COL + 0.5)
INSERT_ARROW_BUTTON_Y = Y_START + SQUARE_SIZE * (NUMBER_OF_ROW - 1)

# all the parameters for the insert arrow window
INSERT_WINDOW_X = WINDOW_X + WINDOW_WIDTH
INSERT_WINDOW_Y = WINDOW_Y
INSERT_WINDOW_LENGTH = WINDOW_LENGTH // 2
INSERT_WINDOW_WIDTH = WINDOW_WIDTH // 2

BUTTON_SIZE = 100
INSERT_WINDOW_CENTER_X = (INSERT_WINDOW_WIDTH // 2) - (BUTTON_SIZE // 2)
INSERT_WINDOW_CENTER_Y = (INSERT_WINDOW_LENGTH // 2) - (BUTTON_SIZE // 2)
RADIOS = INSERT_WINDOW_CENTER_X - 30

UP_BUTTON_X = INSERT_WINDOW_CENTER_X
UP_BUTTON_Y = INSERT_WINDOW_CENTER_Y - RADIOS

UP_RIGHT_BUTTON_X = INSERT_WINDOW_CENTER_X + math.cos(math.pi/4)*RADIOS
UP_RIGHT_BUTTON_Y = INSERT_WINDOW_CENTER_Y - math.sin(math.pi/4)*RADIOS

RIGHT_BUTTON_X = INSERT_WINDOW_CENTER_X + RADIOS
RIGHT_BUTTON_Y = INSERT_WINDOW_CENTER_Y

DOWN_RIGHT_BUTTON_X = INSERT_WINDOW_CENTER_X + math.cos((7*math.pi)/4)*RADIOS
DOWN_RIGHT_BUTTON_Y = INSERT_WINDOW_CENTER_Y - math.sin((7*math.pi)/4)*RADIOS

DOWN_BUTTON_X = INSERT_WINDOW_CENTER_X
DOWN_BUTTON_Y = INSERT_WINDOW_CENTER_Y + RADIOS

DOWN_LEFT_BUTTON_X = INSERT_WINDOW_CENTER_X + math.cos((5*math.pi)/4)*RADIOS
DOWN_LEFT_BUTTON_Y = INSERT_WINDOW_CENTER_Y - math.sin((5*math.pi)/4)*RADIOS

LEFT_BUTTON_X = INSERT_WINDOW_CENTER_X - RADIOS
LEFT_BUTTON_Y = INSERT_WINDOW_CENTER_Y

UP_LEFT_BUTTON_X = INSERT_WINDOW_CENTER_X + math.cos((3*math.pi)/4)*RADIOS
UP_LEFT_BUTTON_Y = INSERT_WINDOW_CENTER_Y - math.sin((3*math.pi)/4)*RADIOS
