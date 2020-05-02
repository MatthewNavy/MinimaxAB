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
        # player is 1 (agent) or 2 (human), 1 goes first
        self.player = 1

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
        copy.player = deepcopy(self.player)
        #copy.player = deepcopy(self.player)
        return copy

    # update game with move given
    # returns whether move was valid or not
    def makeMove(self, move):
        if move in self.getValidMoves():
            row, col = move
            self.validMoves.remove(move)
            #print('making move', move, 'at x =', x, 'y =', y)
            if self.player == 1:
                self.board[row][col] = 1
                self.player = 2
                return True
                #self.player = 2
            elif self.player == 2:
                self.board[row][col] = -1
                self.player = 1
                return True
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
        botScore1 = self.checkDiag1Bot()
        humanScore1 = self.checkDiag1Human()
        botScore2 = self.checkDiag2Bot()
        humanScore2 = self.checkDiag2Human()
        if botScore1 == 1 or botScore2 == 1:
            return 1
        # human wins
        if humanScore1 == -1 or humanScore2 == -1:
            return -1
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
    def checkDiag1Bot(self):
        for i in range(3):
            if self.board[i][i] != 1:
                return 0
        return 1

    def checkDiag2Bot(self):
        for i in range(3):
            if self.board[i][2 - i] != 1:
                return 0
        return 1

    # checks for diagonal win for human
    def checkDiag1Human(self):
        for i in range(3):
            if self.board[i][i] != -1:
                return 0
        return -1
    def checkDiag2Human(self):
        for i in range(3):
            if self.board[i][2 - i] != -1:
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
        botScore1 = self.checkDiag1Bot()
        humanScore1 = self.checkDiag1Human()
        botScore2 = self.checkDiag2Bot()
        humanScore2 = self.checkDiag2Human()
        if botScore1 == 1 or botScore2 == 1:
            return True
        # human wins
        if humanScore1 == -1 or humanScore2 == -1:
            return True
        if len(self.validMoves) == 0:
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