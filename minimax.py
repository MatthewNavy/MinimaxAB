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
        temp = bestMove
        validMoves.add(bestMove)
        for move in validMoves:
            nextValue = self.computeValue(move, 0)
            if nextValue > bestValue:
                bestMove = move
                bestValue = nextValue
        if temp == bestMove:
            print('did not select best move most likely')
        self.gameState.makeMove(bestMove)
        return bestMove

    # compute and return the score of a move
    def computeValue(self, move, depth):
        if self.gameState.isTerminal():
            return self.gameState.scoreGame()
        if depth < self.depth:
            print('depth =', depth)
            nextGameState = self.gameState.copy()
            #self.gameState = nextGameState
            #print(self.gameState)
            #if self.gameState.isTerminal():
                #print('game simulation ended')
                #return self.gameState.scoreGame()
            if nextGameState.player == 2:
                isMade = nextGameState.makeMove(move)
                max = self.computeMax(nextGameState, depth + 1)
                nextGameState.makeMove(move)
                print('computing max')
                return max
            elif nextGameState.player == 1:
                isMade = nextGameState.makeMove(move)
                min = self.computeMin(nextGameState, depth + 1)
                nextGameState.makeMove(move)
                print('computing min')
                return min
            else:
                raise ValueError
        else:
            print('estimating')
            return self.scoreEstimate()

    # compute the value for a max node
    def computeMax(self, newState, depth):
        maxValue = -2
        for nextMove in newState.getValidMoves():
            value = self.computeValue(nextMove, depth)
            if value > maxValue:
                maxValue = value
        return maxValue

    # compute the value for a min node
    def computeMin(self, newState, depth):
        minValue = 2
        for nextMove in newState.getValidMoves():
            value = self.computeValue(nextMove, depth)
            if value < minValue:
                minValue = value
        return minValue

    # if depth reached, give estimate for who will in
    # TODO: add heuristic
    def scoreEstimate(self):
        return random.randint(-1, 1)