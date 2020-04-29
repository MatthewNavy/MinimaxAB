# Matthew Barton

from checkers import Checkers
from minimax import Minimax
from tictactoe import TicTacToe

if __name__ == '__main__':
    print('Starting tic-tac-toe game...')
    game = TicTacToe()
    agent = Minimax(game)
    game.printBoard()

    # game loop
    while not game.isTerminal():
        #agentMove = agent.getMove()
        #game.makeMove(agentMove)
        #print('AI makes move: ' + agentMove)
        humanMove = int(input('Enter a move to make (from 0 - 8): '))
        game.makeMove(humanMove)
        game.printBoard()


    print('Starting Checkers game...')
    game = Checkers()
    agent = Minimax(game)


    print('Program terminated')