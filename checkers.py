# Matthew Barton

from copy import deepcopy

class Checkers:

    # constructor
    def __init__(self):
        self.name = "Checkers"
        # player is 1 or 2, 1 goes first
        self.player = 1
        # 0 = empty space, 1 = black (player 1), -1 = white (player 2)
        # 2 and -2 are kings
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [-1, 0, -1, 0, -1, 0, -1, 0],
                      [0, -1, 0, -1, 0, -1, 0, -1],
                      [-1, 0, -1, 0, -1, 0, -1, 0]]
        # init valid moves as tuples
        self.validMoves = set()
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == -1:
                    self.validMoves.add((row, col))
        # init valid moves as tuples
        self.validMovesHuman = set()
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == 1:
                    self.validMovesHuman.add((row, col))
        # capture totals
        self.player1Score = 0
        self.player2Score = 0

    # copy constructor
    def copy(self):
        copy = Checkers()
        validMoves = set()
        for validMove in self.validMoves:
            validMoves.add(validMove)
        board = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, -1, 0, -1, 0, -1, 0], [0, -1, 0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, 0, -1, 0]]
        for row in range(8):
            for col in range(8):
                board[row][col] = self.board[row][col]

        validMovesHuman = set()
        for validMove in self.validMovesHuman:
            validMoves.add(validMove)
        board = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, -1, 0, -1, 0, -1, 0], [0, -1, 0, -1, 0, -1, 0, -1],
                 [-1, 0, -1, 0, -1, 0, -1, 0]]
        for row in range(8):
            for col in range(8):
                board[row][col] = self.board[row][col]
        copy.validMovesHuman = validMovesHuman
        copy.board = board
        copy.validMoves = validMoves
        copy.player = deepcopy(self.player)
        copy.player1Score = deepcopy(self.player1Score)
        copy.player2Score = deepcopy(self.player2Score)
        return copy

    # makes a move on the board; returns whether move was valid or not
    def makeMove(self, move):
        row, col = move
        if self.player == 1:
            if move in self.getValidMoves():
                # TODO: move logic
                return True
            else:
                return False
        elif self.player == 2:
            if move in self.getValidMovesHuman():
                # TODO: move logic for human
                return True
            else:
                return False
        raise ValueError

    # scores the game after it reaches a terminal state
    def scoreGame(self):
        return self.player1Score - self.player2Score

    # returns whether game is over or not
    def isTerminal(self):
        return self.player1Score == 12 or self.player2Score == 12

    def getValidMovesHuman(self):
        return self.validMovesHuman

    # returns valid moves available for agent
    def getValidMoves(self):
        return self.validMoves