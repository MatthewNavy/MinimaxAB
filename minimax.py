# Matthew Barton

# -1 = loss, 0 = tie, 1 = win
# gameState contains: validMoves(), isTerminal(), scoreGame(), makeMove(move)

class Minimax:

    def __init__(self, gameState):
        self.gameState = gameState
        # assumed that player 1 will run minimax
        self.player = 1

    def computevalue(self, move):
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

    def computeMax(self):
        maxValue = -2
        for nextMove in self.gameState.validMoves():
            value = self.computeValue(nextMove)
            if value > maxValue:
                maxValue = value
        return maxValue

    def computeMin(self):
        minValue = 2
        for nextMove in self.gameState.validMoves():
            value = self.computeValue(nextMove)
            if value < minValue:
                minValue = value
        return minValue

    def computevalue(self,):
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
