# Matthew Barton

from checkers import Checkers
from minimax import Minimax
from tictactoe import TicTacToe
import pygame

# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen size defintions
width = 900
height = 900

if __name__ == '__main__':
    # pygame and window initializaiont
    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()

    # draw empty board
    screen.fill(BLACK)
    lineWidth = 3
    pygame.draw.line(screen, WHITE, [width / 3, 0], [width / 3, height], lineWidth)
    pygame.draw.line(screen, WHITE, [width / 3 * 2, 0], [width / 3 * 2, height], lineWidth)
    pygame.draw.line(screen, WHITE, [0, height / 3], [width, height / 3], lineWidth)
    pygame.draw.line(screen, WHITE, [0, height / 3 * 2], [width, height / 3 * 2], lineWidth)

    # set up game and agent
    print('Starting tic-tac-toe game...')
    game = TicTacToe()
    agent = Minimax(game, 3)
    #game.printBoard()

    # game loop
    gameOver = False
    while not gameOver:
        # reset screen
        #screen.fill(BLACK)

        # get and make ai agent move
        agentMove = agent.getMove()
        game.makeMove(agentMove)
        gameOver = game.isTerminal()
        print('AI makes move: ' + str(agentMove))
        # update screen
        pygame.display.flip()

        #humanMove = int(input('Enter a move to make (from 0 - 8): '))
        # check to see if agent didn't finish game
        if not gameOver:
            # get human input and process moves
            for event in pygame.event.wait():
                # user quits game
                if event.type == pygame.QUIT:
                    print("User ended game.")
                    gameOver = True
                # user makes move
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("User made move")
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    circleColor = WHITE
                    circleWidth = 2
                    # top left corner
                    if x < width / 3 and y < height / 3:
                        humanMove = 0
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [0, 0, width / 3, height / 3], circleWidth)
                    # top middle
                    elif x < width / 3 * 2 and x > width / 3 and y < height / 3:
                        humanMove = 1
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [width / 3, 0, width / 3, height / 3], circleWidth)
                    # top left corner
                    elif x > width / 3 * 2 and y < height / 3:
                        humanMove = 2
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, 0, width / 3, height / 3], circleWidth)
                    # middle left
                    elif x < width / 3 and y > height / 3 and y < height / 3 * 2:
                        humanMove = 3
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [0, height / 3, width / 3, height / 3], circleWidth)
                    # true middle
                    elif x > width / 3 and x < width / 3 * 2 and y > height / 3 and y < height / 3 * 2:
                        humanMove = 4
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [width / 3, height / 3, width / 3, height / 3], circleWidth)
                    # middle right
                    elif x > width / 3 * 2 and y > height / 3 and y < height / 3 * 2:
                        humanMove = 5
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, height / 3, width / 3, height / 3], circleWidth)
                    # bottom right corner
                    elif x < width / 3 and y > height / 3 * 2:
                        humanMove = 6
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [0, height / 3 * 2, width / 3, height / 3], circleWidth)
                    # middle bottom
                    elif x > width / 3 and x < width / 3 * 2 and y > height / 3 * 2:
                        humanMove = 7
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [width / 3, height / 3 * 2, width / 3, height / 3], circleWidth)
                    # bottom right corner
                    elif x > width / 3 * 2 and y > height / 3 * 2:
                        humanMove = 8
                        game.makeMove(humanMove)
                        pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, height / 3 * 2, width / 3, height / 3], circleWidth)
                    gameOver = game.isTerminal()
                    #game.printBoard()
            # update screen
            pygame.display.flip()
        # frames per second = 24
        clock.tick(24)

    # end game
    pygame.quit()

    print('Starting Checkers game...')
    game = Checkers()
    agent = Minimax(game, 3)

    print('Program terminated')