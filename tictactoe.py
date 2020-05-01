# Matthew Barton

from copy import deepcopy

class TicTacToe:

    # constructor
    def __init__(self):
        # init all valid moves as tuples
        self.validMoves = set()
        for row in range(3):
            for col in range(3):
                self.validMoves.add((row, col))
        # 0 = empty space, 1 = X (player 1), -1 = O (player 2)
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # player is 1 or 2, 1 goes first
        #self.player = 1

    # copy constructor
    def copy(self):
        copy = TicTacToe()
        validMoves = set()
        for validMove in self.validMoves:
            validMoves.add(validMove)
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for row in range(3):
            for col in range(3):
                board[row][col] = self.board[row][col]
        copy.validMoves = validMoves
        copy.board = board
        #copy.player = deepcopy(self.player)
        return copy

    # update game with move given
    # returns whether move was valid or not
    def makeMove(self, move, player):
        if move in self.getValidMoves():
            row, col = move
            self.validMoves.remove(move)
            #print('making move', move, 'at x =', x, 'y =', y)
            if player == 1:
                self.board[row][col] = 1
                return True
                #self.player = 2
            elif player == 2:
                self.board[row][col] = -1
                return True
                #self.player = 1
            else:
                raise ValueError
        return False

    # assumed that state is terminal
    # returns who won the game
    def scoreGame(self):
        for row in range(3):
            botScore = self.checkRowBot(row)
            humanScore = self.checkRowHuman(row)
            # bot wins
            if botScore == 1:
                return botScore
            # human wins
            if humanScore == -1:
                return humanScore
        for col in range(3):
            botScore = self.checkColBot(col)
            humanScore = self.checkColHuman(col)
            # bot wins
            if botScore == 1:
                return botScore
            # human wins
            if humanScore == -1:
                return humanScore
        botScore = self.checkDiagsBot()
        humanScore = self.checkDiagsHuman()
        if botScore == 1:
            return botScore
        # human wins
        if humanScore == -1:
            return humanScore
        return 0  # a tie

    # checks for row win for bot
    def checkRowBot(self, row):
        for col in range(3):
            if self.board[row][col] != 1:
                return 0
        return 1

    # checks for row win for human
    def checkRowHuman(self, row):
        for col in range(3):
            if self.board[row][col] != -1:
                return 0
        return -1

    # checks for column win for bot
    def checkColBot(self, col):
        for row in range(3):
            if self.board[row][col] != 1:
                return 0
        return 1

    # checks for column win for human
    def checkColHuman(self, col):
        for row in range(3):
            if self.board[row][col] != -1:
                return 0
        return -1

    # checks for diagonal win for bot
    def checkDiagsBot(self):
        for i in range(3):
            if self.board[i][i] != 1 and self.board[i][2-i] != 1:
                return 0
        return 1

    # checks for diagonal win for human
    def checkDiagsHuman(self):
        for i in range(3):
            if self.board[i][i] != -1 and self.board[i][2-i] != -1:
                return 0
        return -1

    # returns non-empty board positions
    def getValidMoves(self):
        return self.validMoves

    # returns whether game is over or not
    # cannot use scoreGame since not guranteed to be terminal (obviously, given the function name)
    def isTerminal(self):
        for row in range(3):
            botScore = self.checkRowBot(row)
            humanScore = self.checkRowHuman(row)
            # bot wins
            if botScore == 1:
                return True
            # human wins
            if humanScore == -1:
                return True
        for col in range(3):
            botScore = self.checkColBot(col)
            humanScore = self.checkColHuman(col)
            # bot wins
            if botScore == 1:
                return True
            # human wins
            if humanScore == -1:
                return True
        botScore = self.checkDiagsBot()
        humanScore = self.checkDiagsHuman()
        if botScore == 1:
            return True
        # human wins
        if humanScore == -1:
            return True
        return False

    # debug print
    def printBoard(self):
        sep = 0
        for row in range(3):
            spaces = []
            for col in range(3):
                space = self.board[row][col]
                if space == -1:
                    spaces.append("O")
                elif space == 1:
                    spaces.append("X")
                else:
                    spaces.append(" ")
            sep += 1
            if sep < 3:
                print(spaces[0], "|", spaces[1], "|", spaces[2], "\n---------")
            else:
                print(spaces[0], "|", spaces[1], "|", spaces[2])