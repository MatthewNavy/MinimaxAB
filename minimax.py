# Matthew Barton

# -1 = loss, 0 = tie, 1 = win
# gameState contains: validMoves(), isTerminal(), scoreGame(), makeMove(move)

class Minimax:

    # constructor
    def __init__(self, gameState, depth):
        self.gameState = gameState
        # assumed that player 1 will run minimax
        self.player = 1
        # how far down the tree it will search
        self.depth = depth

    # get the best move for the current gamestate using the minimax algorithm; starts the minimax tree
    def getMove(self):
        bestMove = -1
        bestValue = -1
        for move in self.gameState.getValidMoves():
            if move != -1:
                nextValue = self.computeValue(move, 0)
                if nextValue > bestValue:
                    bestMove = move
                    bestValue = nextValue
        return bestMove

    # compute and return the score of a move
    def computeValue(self, move, depth):
        if depth < self.depth:
            nextGameState = self.gameState.copy()
            nextGameState.makeMove(move)
            self.gameState = nextGameState
            #print(self.gameState)
            if self.gameState.isTerminal():
                print('game simulation ended')
                return self.gameState.scoreGame()
            elif self.player == 1:
                self.player = 2
                print('computing max')
                return self.computeMax(depth)
            elif self.player == 2:
                self.player = 1
                print('computing min')
                return self.computeMin(depth)
            else:
                raise ValueError
        else:
            return 0

    # compute the value for a max node
    def computeMax(self, depth):
        maxValue = -2
        for nextMove in self.gameState.getValidMoves():
            if nextMove != -1:
                value = self.computeValue(nextMove, depth + 1)
                if value > maxValue:
                    maxValue = value
        return maxValue

    # compute the value for a min node
    def computeMin(self, depth):
        minValue = 2
        for nextMove in self.gameState.getValidMoves():
            if nextMove != -1:
                value = self.computeValue(nextMove, depth + 1)
                if value < minValue:
                    minValue = value
        return minValue
