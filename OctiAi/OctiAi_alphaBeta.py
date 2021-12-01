import json
import math
from OctiModel.Enums import *
from OctiModel.BoardGame import *
import random

""" This AI is working according to the alpha beta algorithm.
    Remember the AI is the green player!! 
    The number of states the AI need to search is something like 32^(2*depth) """

class OctiAi_alphaBeta:
    """ Constants """
    __DEPTH = 2     # how many layers the alpha beta algorithm will search
    __BIAS = 32     # an average number of possible action in a turn.

    """ Constructor """
    def __init__(self, board):
        self.__AiBoard = board
        self.__randomBias = 0

    """ return a jason of the state that the AI will choose. The best decision against an optimal enemy,
        within depth = __DEPTH  steps"""
    def alphaBetaSearch(self, state):
        return self.__maxValue(state, -math.inf, math.inf, self.__DEPTH)[0]

    """ take care of the maximum states. return a tuple of (state, value) """
    def __maxValue(self, state, alpha, beta, depth):
        self.__AiBoard.jsonToBoard(state)     # make the AI Board game update to state

        # if the state is terminal state return the evaluation, or if depth equal to zero
        if self.__AiBoard.isGoalState() is not None or depth == 0:
            return state, self.__evaluation(state)

        #explored = set()    # a hash table that save all the state the has been explored already in the layer.
        stateAndValue = (state, -math.inf)
        for nextState in self.__AiBoard.getSuccessors():
            #if nextState not in explored:
                #if depth != self.__DEPTH:
                    #explored.add(nextState)

            # at the beginning set a new bias for every possible action.
            # it help to choose the preferred state among equal states
            if depth == self.__DEPTH:
                self.setNewBias()
                print("--\n", self.__randomBias)

            newValue = max(stateAndValue[1], self.__minValue(nextState, alpha, beta, depth)[1])
            if newValue != stateAndValue[1]:
                stateAndValue = (nextState, newValue)
            # pruning occurred
            if stateAndValue[1] >= beta:
                return stateAndValue
            alpha = max(alpha, stateAndValue[1])    # update alpha
        return stateAndValue

    """ take care of the minimum states. return a tuple of (state, value) """
    def __minValue(self, state, alpha, beta, depth):
        self.__AiBoard.jsonToBoard(state)     # make the AI Board game update to state

        # if the state is terminal state return the evaluation, or if depth equal to zero
        if self.__AiBoard.isGoalState() is not None or depth == 0:
            return state, self.__evaluation(state)

        #explored = set()  # a hash table that save all the state the has been explored already in the layer.
        stateAndValue = (state, math.inf)
        for nextState in self.__AiBoard.getSuccessors():
            #if nextState not in explored:
                #if depth != self.__DEPTH:
                    #explored.add(nextState)

            newValue = min(stateAndValue[1], self.__maxValue(nextState, alpha, beta, depth - 1)[1])
            if newValue != stateAndValue[1]:
                stateAndValue = (nextState, newValue)
            # pruning occurred
            if stateAndValue[1] <= alpha:
                return stateAndValue
            beta = min(beta, stateAndValue[1])    # update beta
        return stateAndValue

    """ set a  """
    def setNewBias(self):
        self.__randomBias = random.randrange(1, self.__BIAS)

    """evaluate a number according to the worth of a state.
       return a double """
    def __evaluation(self, state):
        """TODO: together"""
        self.__AiBoard.jsonToBoard(state)
        if self.__AiBoard.isGoalState() == Players.Green:
            return 1000000     # if the AI win, remember the AI is the green player
        elif self.__AiBoard.isGoalState() == Players.Red:
            return -1000000    # if the AI lose, remember the opponent of the AI is the red player

        evaluation = 0  # the number that represent the evaluation

        allGreenOct = self.__AiBoard.namesOfAllPlayerAliveOct(Players.Green)
        allRedOct = self.__AiBoard.namesOfAllPlayerAliveOct(Players.Red)

        # green oct (the AI's octs) life worth 120, and red oct(opponent's octs) worth -100
        evaluation = len(allGreenOct) * (120) + len(allRedOct) * (-100)

        for oct in allGreenOct:
            evaluation += self.__evaluate_arrows(oct)

        nearest_oct = self.__find_nearest_oct_to_goal(allGreenOct)
        evaluation += self.__evaluate_distance(nearest_oct)


        # use random to choose the preferred state among equal states.
        evaluation = evaluation + 1/self.__randomBias

        return evaluation

    def __evaluate_arrows(self, oct:str):
        score = 0
        arrows = self.__AiBoard.allArrows(oct)
        for arrow in arrows:
            if arrow == Directions.Down:
                score += 5
            elif arrow == Directions.DownLeft or arrow == Directions.DownRight:
                score += 4
            elif arrow == Directions.Left or arrow == Directions.Right:
                score += 3
            else:
                score += 2

            # optimal number of arrows for an oct is 3 arrows
            if len(arrows) == 3:
                score *= 1.5

        return score

    def __find_nearest_oct_to_goal(self, octs:list[str]):
        nearest = octs[0]
        nearest_steps = self.__AiBoard.numberOfStepsToGoal(nearest)
        for i in range(1, len(octs)):
            current_steps = self.__AiBoard.numberOfStepsToGoal(octs[i])
            if nearest_steps > current_steps:
                nearest = octs[i]
                nearest_steps = current_steps

        return nearest

    def __evaluate_distance(self, oct):
        """ the more arrows the nearest oct to gaol has, the better.
            i.e - (number of arrows) * (15/steps + 0.0001).
            The 0.0001 is because that the number of steps can be zero, and we don't want to divide by zero"""
        return 15/(self.__AiBoard.numberOfStepsToGoal(oct) + 0.0001) * len(self.__AiBoard.allArrows(oct))


