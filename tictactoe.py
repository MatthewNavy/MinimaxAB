# Matthew Barton

class TicTacToe:

    # constructor
    def __init__(self):
        # board indexed from 0 to 8, -1 means invalid
        self.validMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # 0 = empty space, 1 = X (player 1), -1 = O (player 2)
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # player is 1 or 2, 1 goes first
        self.player = 1

    # copy constructor
    def copy(self):
        copy = TicTacToe()
        copy.validMoves = self.validMoves.copy()
        copy.board = self.board.copy()
        copy.player = self.player
        return copy

    # update game with move given
    def makeMove(self, move):
        x = move % 3
        y = move // 3
        #print("x =", str(x), "y =", str(y))
        if self.player == 1:
            self.board[x][y] = 1
            self.player = 2
        elif self.player == 2:
            self.board[x][y] = -1
            self.player = 1
        else:
            raise ValueError

    # assumed that state is terminal
    # returns who won the game
    def scoreGame(self):
        score = 0
        for row in range(3):
            for col in range(3):
                botScore = self.checkForThreeBot(row, col, 0)
                humanScore = self.checkForThreeHuman(row, col, 0)
                # bot wins
                if botScore == 1:
                    return botScore
                # human wins
                if humanScore == -1:
                    return humanScore
        return score  # score = 0, a tie

    # check for a triple given any position on the board
    # only works for agent, so you need to invert for human player score
    # returns 1 if agent won, 0 if tied or ongoing
    def checkForThreeBot(self, row, col, scoreCounter):
        if scoreCounter == 3:
            return 1
        # elif row < 0 or col < 0 or row > 2 or col > 2:
        #     return 0
        foundNext = False
        for i in range(3):
            for j in range(3):
                if i != j and row + i >= 0 and row + i < 3 and col + j >= 0 and col + j < 3 and self.board[row + i][col + j] == 1:
                    foundNext = True
                    return self.checkForThreeBot(row + i, col + j, scoreCounter + 1)
        if not foundNext:
            return 0

    # check for a triple given any position on the board
    # only works for human, so you need to invert for agent player score
    # returns -1 if human won, 0 if tied or ongoing
    def checkForThreeHuman(self, row, col, scoreCounter):
        if scoreCounter == 3:
            return -1
        # elif row < 0 or col < 0 or row > 2 or col > 2:
        #     return 0
        foundNext = False
        for i in range(3):
            for j in range(3):
                if i != j and row + i >= 0 and row + i < 3 and col + j >= 0 and col + j < 3 and self.board[row + i][col + j] == -1:
                    foundNext = True
                    return self.checkForThreeHuman(row + i, col + j, scoreCounter + 1)
        if not foundNext:
            return 0

    # returns non-empty board positions
    def getValidMoves(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] != 0:
                    #print("row =", str(row), "col =", str(col))
                    self.validMoves[row + col] = -1
        return self.validMoves

    # returns whether game is over or not
    # cannot use scoreGame since not guranteed to be terminal (obviously, given the function name)
    def isTerminal(self):
        for row in range(3):
            for col in range(3):
                if self.checkForThreeBot(row, col, 0) != 0:
                    return True
                if self.checkForThreeHuman(row, col, 0) != 0:
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