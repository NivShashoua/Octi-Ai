import json
import math
from OctiModel.Enums import *
from OctiModel.BoardGame import *
import random

""" This AI is working according to the alpha beta algorithm.
    Remember the AI is the green player!! 
    The number of states the AI need to search is something like 32^(2*depth) """

class OctiAi:
    """ Constants """
    __DEPTH = 3     # how many layers the alpha beta algorithm will search
    __BIAS = 32

    """ Constructor """
    def __init__(self, board):
        self.__AiBoard = board

    """ return the state that the AI will choose. The best decision against an optimal enemy,
        with depth = __DEPTH  steps"""
    def alphaBetaSearch(self, state):
        return self.__maxValue(state, -math.inf, math.inf, self.__DEPTH)[0]

    """ take care of the maximum states. return a tuple of (state, value) """
    def __maxValue(self, state, alpha, beta, depth):
        self.__AiBoard.stringToBoard(state)     # make the AI Board game update to state

        # if the state is terminal state return the evaluation, or if depth equal to zero
        if self.__AiBoard.isGoalState() is not None or depth == 0:
            return state, self.__evaluation(state)

        stateAndValue = (state, -math.inf)
        for nextState in self.__AiBoard.getSuccessors():
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
        self.__AiBoard.stringToBoard(state)     # make the AI Board game update to state

        # if the state is terminal state return the evaluation, or if depth equal to zero
        if self.__AiBoard.isGoalState() is not None or depth == 0:
            return state, self.__evaluation(state)

        stateAndValue = (state, math.inf)
        for nextState in self.__AiBoard.getSuccessors():
            newValue = min(stateAndValue[1], self.__maxValue(nextState, alpha, beta, depth - 1)[1])
            if newValue != stateAndValue[1]:
                stateAndValue = (nextState, newValue)
            # pruning occurred
            if stateAndValue[1] <= alpha:
                return stateAndValue
            beta = min(beta, stateAndValue[1])    # update beta
        return stateAndValue

    """evaluate a number according to the worth of a state.
       return a double """
    def __evaluation(self, state):
        """TODO: together"""
        self.__AiBoard.stringToBoard(state)
        if self.__AiBoard.isGoalState() == Players.Green:
            return math.inf     # if the AI win, remember the AI is the green player
        elif self.__AiBoard.isGoalState() == Players.Red:
            return -math.inf    # if the AI lose, remember the opponent of the AI is the red player

        evaluation = 0  # the number that represent the evaluation

        allGreenOct = self.__AiBoard.namesOfAllPlayerAliveOct(Players.Green)
        allRedOct = self.__AiBoard.namesOfAllPlayerAliveOct(Players.Red)

        # green oct (the AI's octs) life worth 120, and red oct(opponent's octs) worth -100
        evaluation = len(allGreenOct) * (120 + self.__BIAS) + len(allRedOct) * (-100 + self.__BIAS)

        # use random to choose the preferred state among equal states.
        evaluation = evaluation + random.randrange(self.__BIAS)

        return evaluation
