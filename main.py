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

def promptUserAndMakeMove(pos):
    #print("User made move")
    x = pos[0]
    y = pos[1]
    circleColor = WHITE
    circleWidth = 2
    print(game.getValidMoves())
    # top left corner
    if x < width / 3 and y < height / 3:
        humanMove = (0, 0)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [0, 0, width / 3, height / 3], circleWidth)
    # top middle
    elif x < width / 3 * 2 and x > width / 3 and y < height / 3:
        humanMove = (0, 1)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [width / 3, 0, width / 3, height / 3], circleWidth)
    # top right corner
    elif x > width / 3 * 2 and y < height / 3:
        humanMove = (0, 2)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, 0, width / 3, height / 3], circleWidth)
    # middle left
    elif x < width / 3 and y > height / 3 and y < height / 3 * 2:
        humanMove = (1, 0)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [0, height / 3, width / 3, height / 3], circleWidth)
    # true middle
    elif x > width / 3 and x < width / 3 * 2 and y > height / 3 and y < height / 3 * 2:
        humanMove = (1, 1)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [width / 3, height / 3, width / 3, height / 3], circleWidth)
    # middle right
    elif x > width / 3 * 2 and y > height / 3 and y < height / 3 * 2:
        humanMove = (1, 2)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, height / 3, width / 3, height / 3], circleWidth)
    # bottom left corner
    elif x < width / 3 and y > height / 3 * 2:
        humanMove = (2, 0)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [0, height / 3 * 2, width / 3, height / 3], circleWidth)
    # middle bottom
    elif x > width / 3 and x < width / 3 * 2 and y > height / 3 * 2:
        humanMove = (2, 1)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [width / 3, height / 3 * 2, width / 3, height / 3], circleWidth)
    # bottom right corner
    elif x > width / 3 * 2 and y > height / 3 * 2:
        humanMove = (2, 2)
        if humanMove in game.getValidMoves():
            game.makeMove(humanMove, 2)  # human is player 2
            pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, height / 3 * 2, width / 3, height / 3], circleWidth)

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
    agent = Minimax(game, 1)
    #game.printBoard()

    # game loop
    gameOver = False
    while not gameOver:
        # reset screen
        #screen.fill(BLACK)
        game.printBoard()

        # get and make ai agent move
        agentMove = agent.getMove()
        game.makeMove(agentMove, 1)  # bot is player 1
        gameOver = game.isTerminal()
        print(gameOver)
        print('AI makes move: ' + str(agentMove))

        # draw ai agent move
        xColor = WHITE
        xWidth = 2
        # top left corner
        if agentMove == 0:
            pygame.draw.line(screen, xColor, [0, 0], [width / 3, height / 3], xWidth)
            pygame.draw.line(screen, xColor, [0, height / 3], [width / 3, 0], xWidth)
        # top middle
        if agentMove == 1:
            pygame.draw.line(screen, xColor, [width / 3, 0], [width / 3 * 2, height / 3], xWidth)
            pygame.draw.line(screen, xColor, [width / 3, height / 3], [width / 3 * 2, 0], xWidth)
        # top right corner
        if agentMove == 2:
            pygame.draw.line(screen, xColor, [width / 3 * 2, 0], [width, height / 3], xWidth)
            pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3], [width, 0], xWidth)
        # middle left
        if agentMove == 3:
            pygame.draw.line(screen, xColor, [0, height / 3], [width / 3, height / 3 * 2], xWidth)
            pygame.draw.line(screen, xColor, [0, height / 3 * 2], [width / 3, height / 3], xWidth)
        # true middle
        if agentMove == 4:
            pygame.draw.line(screen, xColor, [width / 3, height / 3], [width / 3 * 2, height / 3 * 2], xWidth)
            pygame.draw.line(screen, xColor, [width / 3, height / 3 * 2], [width / 3 * 2, height / 3], xWidth)
        # middle right
        if agentMove == 5:
            pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3], [width, height / 3 * 2], xWidth)
            pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3 * 2], [width, height / 3], xWidth)
        # bottom left corner
        if agentMove == 6:
            pygame.draw.line(screen, xColor, [0, height / 3 * 2], [width / 3, height], xWidth)
            pygame.draw.line(screen, xColor, [0, height], [width / 3, height / 3 * 2], xWidth)
        # bottom middle
        if agentMove == 7:
            pygame.draw.line(screen, xColor, [width / 3, height / 3 * 2], [width / 3 * 2, height], xWidth)
            pygame.draw.line(screen, xColor, [width / 3, height], [width / 3 * 2, height / 3 * 2], xWidth)
        # bottom right corner
        if agentMove == 8:
            pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3 * 2], [width, height], xWidth)
            pygame.draw.line(screen, xColor, [width / 3 * 2, height], [width, height / 3 * 2], xWidth)

        # update screen
        pygame.display.flip()

        # check to see if agent didn't finish game
        if not gameOver:
            # get human input and process moves
            for event in pygame.event.get():
                # user quits game
                if event.type == pygame.QUIT:
                    print("User ended game.")
                    gameOver = True
                # user makes move
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    promptUserAndMakeMove(pos)
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