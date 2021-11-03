import json
import math

class OctiAi:
    """ Constants """
    __DEPTH = 4   # how many layers the alpha beta algorithm will search

    """ Constructor """
    def __init__(self, board):
        self.__AiBoard = board

    """ return the state that the AI will choose. The best decision against an optimal enemy,
        with depth = __DEPTH  steps"""
    def alphaBetaSearch(self, state):
        return self.__maxValue(state, -math.inf, math.inf, self.__DEPTH)

    """"""
    def __maxValue(self, state, alpha, beta, depth):
        self.__AiBoard.stringToBoard(state)     # make the AI Board game update to state

        # if the state is terminal state return the evaluation, or if depth equal to zero
        if self.__AiBoard.isGoalState() is not None or depth == 0:
            return self.__evaluation(state)

        value = -math.inf
        for nextState in self.__AiBoard.getSuccessors:
            value = max(value, self.__minValue(nextState, alpha, beta, depth - 1))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    """"""
    def __minValue(self, state, alpha, beta, depth):
        """TODO: niv"""

    """"""
    def __evaluation(self,jsonBoard):
        """TODO: together"""
