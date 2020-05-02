# Matthew Barton

# -1 = loss, 0 = tie, 1 = win
# gameState contains: validMoves(), isTerminal(), scoreGame(), makeMove(move)

from time import perf_counter

class Minimax:

    # constructor
    def __init__(self, gameState, depth, prune):
        self.gameState = gameState
        # how far down the tree it will search
        self.depth = depth
        self.nodeCount = 0
        self.prune = prune


    # get the best move for the current gamestate using the minimax algorithm; starts the minimax tree for the current gamestate
    def getMove(self):
        if not self.prune:
            start = perf_counter()
            self.nodeCount = 0
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
            end = perf_counter()
            print('Time taken to compute next move (no pruning): ', end - start)
            self.gameState.makeMove(bestMove)
            print('Number of nodes expanded (no pruning): ', self.nodeCount)
            return bestMove
        else:
            start = perf_counter()
            self.nodeCount = 0
            bestValue = -2
            validMoves = self.gameState.getValidMoves()
            bestMove = validMoves.pop()
            # temp = bestMove
            validMoves.add(bestMove)
            for move in validMoves:
                nextGameState = self.gameState.copy()
                nextGameState.makeMove(move)
                nextValue = self.computeValuePrune(nextGameState, 0, -2, 2)
                if nextValue > bestValue:
                    bestMove = move
                    bestValue = nextValue
            # if temp == bestMove:
            #     print('did not select best move most likely')
            end = perf_counter()
            print('Time taken to compute next move (with pruning): ', end - start)
            self.gameState.makeMove(bestMove)
            print('Number of nodes expanded (with pruning): ', self.nodeCount)
            return bestMove

    # compute and return the score of a move
    def computeValue(self, state, depth):
        self.nodeCount += 1
        if state.isTerminal():
            return state.scoreGame()
        if depth < self.depth:
            print('depth =', depth)
            if state.player == 1:
                max = self.computeMax(state, depth + 1)
                print('computing max')
                return max
            elif state.player == 2:
                min = self.computeMin(state, depth + 1)
                print('computing min')
                return min
            else:
                raise ValueError
        else:
            print('estimating')
            return self.scoreEstimate()

    # compute and return the score of a move
    def computeValuePrune(self, state, depth, alpha, beta):
        self.nodeCount += 1
        if state.isTerminal():
            return state.scoreGame()
        if depth < self.depth:
            print('depth =', depth)
            if state.player == 1:
                max = self.computeMaxPrune(state, depth + 1, alpha, beta)
                print('computing max')
                return max
            elif state.player == 2:
                min = self.computeMinPrune(state, depth + 1, alpha, beta)
                print('computing min')
                return min
            else:
                raise ValueError
        else:
            print('estimating')
            return self.scoreEstimate()

    # compute the value for a max node with ab pruning
    def computeMaxPrune(self, state, depth, alpha, beta):
        maxValue = -2
        for nextMove in state.getValidMoves():
            nextGameState = state.copy()
            nextGameState.makeMove(nextMove)
            value = self.computeValuePrune(nextGameState, depth, beta, max(alpha, maxValue))
            if value > maxValue:
                maxValue = value
                if maxValue >= beta:
                    return maxValue
                alpha = max(alpha, maxValue)
        return maxValue

    # compute the value for a min node with ab pruning
    def computeMinPrune(self, state, depth, alpha, beta):
        minValue = 2
        for nextMove in state.getValidMoves():
            nextGameState = state.copy()
            nextGameState.makeMove(nextMove)
            value = self.computeValuePrune(nextGameState, depth, min(beta, minValue), alpha)
            if value < minValue:
                minValue = value
                if minValue <= alpha:
                    return minValue
                beta = max(beta, minValue)
        return minValue

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