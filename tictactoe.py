# Matthew Barton
from copy import deepcopy

print('Starting tic-tac-toe game...')

class TicTacToe:

    def __init__(self):
        # board indexed from 0 to 8
        self.validMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # 0 = empty space, -1 = X (player 1), 1 = O (player 2)
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # player is 1 or 2, 1 goes first
        self.player = 1

    def copy(self):
        return deepcopy(self)

    def makeMove(self, move):
        if self.player == 1:
            self.board[move] = -1
            self.player = 2
        elif self.player == 2:
            self.board[move] = 1
            self.player = 1
        else:
            raise ValueError


    # assumed that state is terminal
    def scoreGame(self):
        score = 0
        for row in range(3):
            for col in range(3):
                score = self.checkForThree(row, col)
        return score

    # TODO: check for winning game
    def checkForThree(self, row, col):
        space = self.board[row + col]
        if space == -1:
            score = 0

            return score
        elif space == 1:
            score = 0

            return score
        else:
            return 0

    def validMoves(self):
        for space in range(len(self.board)):
            if self.board[space] != 0:
                del self.validMoves[space]
        return self.validMoves

    # TODO: check for terminal game state
    def isTerminal(self):
        return False