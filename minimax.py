# Matthew Barton

# -1 = loss, 0 = tie, 1 = win
# gameState contains: validMoves(), isTerminal(), scoreGame(), makeMove(move)

class Minimax:

    # constructor
    def __init__(self, gameState):
        self.gameState = gameState
        # assumed that player 1 will run minimax
        self.player = 1

    # get the best move for the current gamestate using the minimax algorithm
    def getMove(self):
        bestMove = -1
        bestValue = -1
        for move in self.gameState.getValidMoves():
            nextValue = self.computeValue(move)
            if nextValue > bestValue:
                bestMove = move
                bestValue = nextValue
        return bestMove

    # compute and return the score of a move
    def computeValue(self, move):
        nextGameState = self.gameState.copy()
        nextGameState.makeMove(move)
        self.gameState = nextGameState
        if self.gameState.isTerminal():
            return self.gameState.scoreGame()
        elif self.player == 1:
            self.player = 2
            return self.computeMax()
        elif self.player == 2:
            self.player = 1
            return self.computeMin()
        else:
            raise ValueError

    # compute the value for a max node
    def computeMax(self):
        maxValue = -2
        for nextMove in self.gameState.getValidMoves():
            value = self.computeValue(nextMove)
            if value > maxValue:
                maxValue = value
        return maxValue

    # compute the value for a min node
    def computeMin(self):
        minValue = 2
        for nextMove in self.gameState.getValidMoves():
            value = self.computeValue(nextMove)
            if value < minValue:
                minValue = value
        return minValue
