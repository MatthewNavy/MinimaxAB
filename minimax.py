# Matthew Barton

# -1 = loss, 0 = tie, 1 = win
# gameState contains: validMoves(), isTerminal(), scoreGame(), makeMove(move)

import random

class Minimax:

    # constructor
    def __init__(self, gameState, depth):
        self.gameState = gameState
        # assumed that player 1 will run minimax
        #self.player = 1
        # how far down the tree it will search
        self.depth = depth

    # get the best move for the current gamestate using the minimax algorithm; starts the minimax tree for the current gamestate
    def getMove(self):
        bestValue = -2
        validMoves = self.gameState.getValidMoves()
        bestMove = validMoves.pop()
        # temp = bestMove
        validMoves.add(bestMove)
        for move in validMoves:
            nextGameState = self.gameState.copy()
            nextGameState.makeMove(move)
            nextValue = self.computeValue(nextGameState, 0)
            if nextValue > bestValue:
                bestMove = move
                bestValue = nextValue
        # if temp == bestMove:
        #     print('did not select best move most likely')
        self.gameState.makeMove(bestMove)
        return bestMove

    # compute and return the score of a move
    def computeValue(self, state, depth):
        if state.isTerminal():
            return state.scoreGame()
        if depth < self.depth:
            print('depth =', depth)
            # nextGameState = state.copy()
            # nextGameState.makeMove(move)
            # if nextGameState.isTerminal():
            #     return nextGameState.scoreGame()
            if state.player == 1:
                #isMade = nextGameState.makeMove(move)
                max = self.computeMax(state, depth + 1)
                print('computing max')
                return max
            elif state.player == 2:
                #isMade = nextGameState.makeMove(move)
                min = self.computeMin(state, depth + 1)
                print('computing min')
                return min
            else:
                raise ValueError
        else:
            print('estimating')
            return self.scoreEstimate()

    # compute the value for a max node
    def computeMax(self, state, depth):
        maxValue = -2
        for nextMove in state.getValidMoves():
            nextGameState = state.copy()
            nextGameState.makeMove(nextMove)
            value = self.computeValue(nextGameState, depth)
            if value > maxValue:
                maxValue = value
        return maxValue

    # compute the value for a min node
    def computeMin(self, state, depth):
        minValue = 2
        for nextMove in state.getValidMoves():
            nextGameState = state.copy()
            nextGameState.makeMove(nextMove)
            value = self.computeValue(nextGameState, depth)
            if value < minValue:
                minValue = value
        return minValue

    # if depth reached, give estimate for who will in
    # TODO: add heuristic
    def scoreEstimate(self):
        return 0