# Matthew Barton

class TicTacToe:

    # constructor
    def __init__(self):
        # board indexed from 0 to 8
        self.validMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # 0 = empty space, -1 = X (player 1), 1 = O (player 2)
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # player is 1 or 2, 1 goes first
        self.player = 1

    # copy constructor
    def copy(self):
        copy = TicTacToe()
        copy.validMoves = self.validMoves
        copy.board = self.board
        copy.player = self.player
        return copy

    # update game with move given
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
    # returns who won the game
    def scoreGame(self):
        score = 0
        for row in range(3):
            for col in range(3):
                print("row = ", row, " col = ", col)
                score = self.checkForThree(row, col)
        return score

    # check for a triple given any position on the board
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

    # returns non-empty board positions
    def getValidMoves(self):
        for space in range(len(self.board)):
            if self.board[space] != 0:
                del self.validMoves[space]
        return self.validMoves

    # returns whether game is over or not
    # TODO: check for terminal game state
    def isTerminal(self):
        return False

    # debug print
    def printBoard(self):
        sep = 0
        for row in range(3):
            spaces = []
            for col in range(3):
                space = self.board[row + col]
                if space == -1:
                    spaces.append("X")
                elif space == 1:
                    spaces.append("O")
                else:
                    spaces.append(" ")
            sep += 1
            if sep < 3:
                print(spaces[0], "|", spaces[1], "|", spaces[2], "\n---------")
            else:
                print(spaces[0], "|", spaces[1], "|", spaces[2])