# Matthew Barton

from checkers import Checkers
from minimax import Minimax
from tictactoe import TicTacToe
from time import sleep
import pygame

# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen size defintions
width = 900
height = 900

def promptUserAndMakeMove(pos):
    x = pos[0]
    y = pos[1]
    circleColor = WHITE
    circleWidth = 2
    # top left corner
    if x < width / 3 and y < height / 3:
        humanMove = (0, 0)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [0, 0, width / 3, height / 3], circleWidth)
    # top middle
    elif x < width / 3 * 2 and x > width / 3 and y < height / 3:
        humanMove = (0, 1)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [width / 3, 0, width / 3, height / 3], circleWidth)
    # top right corner
    elif x > width / 3 * 2 and y < height / 3:
        humanMove = (0, 2)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, 0, width / 3, height / 3], circleWidth)
    # middle left
    elif x < width / 3 and y > height / 3 and y < height / 3 * 2:
        humanMove = (1, 0)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [0, height / 3, width / 3, height / 3], circleWidth)
    # true middle
    elif x > width / 3 and x < width / 3 * 2 and y > height / 3 and y < height / 3 * 2:
        humanMove = (1, 1)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [width / 3, height / 3, width / 3, height / 3], circleWidth)
    # middle right
    elif x > width / 3 * 2 and y > height / 3 and y < height / 3 * 2:
        humanMove = (1, 2)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, height / 3, width / 3, height / 3], circleWidth)
    # bottom left corner
    elif x < width / 3 and y > height / 3 * 2:
        humanMove = (2, 0)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [0, height / 3 * 2, width / 3, height / 3], circleWidth)
    # middle bottom
    elif x > width / 3 and x < width / 3 * 2 and y > height / 3 * 2:
        humanMove = (2, 1)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [width / 3, height / 3 * 2, width / 3, height / 3], circleWidth)
    # bottom right corner
    elif x > width / 3 * 2 and y > height / 3 * 2:
        humanMove = (2, 2)
        moveMade = game.makeMove(humanMove)
        if moveMade:
            pygame.draw.ellipse(screen, circleColor, [width / 3 * 2, height / 3 * 2, width / 3, height / 3], circleWidth)

def promptAgentAndMakeMove():
    # get and make ai agent move
    agentMove = agent.getMove()
    moveMade = game.makeMove(agentMove)

    # draw ai agent move
    xColor = WHITE
    xWidth = 2
    # top left corner
    if agentMove == (0, 0):
        pygame.draw.line(screen, xColor, [0, 0], [width / 3, height / 3], xWidth)
        pygame.draw.line(screen, xColor, [0, height / 3], [width / 3, 0], xWidth)
    # top middle
    if agentMove == (0, 1):
        pygame.draw.line(screen, xColor, [width / 3, 0], [width / 3 * 2, height / 3], xWidth)
        pygame.draw.line(screen, xColor, [width / 3, height / 3], [width / 3 * 2, 0], xWidth)
    # top right corner
    if agentMove == (0, 2):
        pygame.draw.line(screen, xColor, [width / 3 * 2, 0], [width, height / 3], xWidth)
        pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3], [width, 0], xWidth)
    # middle left
    if agentMove == (1, 0):
        pygame.draw.line(screen, xColor, [0, height / 3], [width / 3, height / 3 * 2], xWidth)
        pygame.draw.line(screen, xColor, [0, height / 3 * 2], [width / 3, height / 3], xWidth)
    # true middle
    if agentMove == (1, 1):
        pygame.draw.line(screen, xColor, [width / 3, height / 3], [width / 3 * 2, height / 3 * 2], xWidth)
        pygame.draw.line(screen, xColor, [width / 3, height / 3 * 2], [width / 3 * 2, height / 3], xWidth)
    # middle right
    if agentMove == (1, 2):
        pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3], [width, height / 3 * 2], xWidth)
        pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3 * 2], [width, height / 3], xWidth)
    # bottom left corner
    if agentMove == (2, 0):
        pygame.draw.line(screen, xColor, [0, height / 3 * 2], [width / 3, height], xWidth)
        pygame.draw.line(screen, xColor, [0, height], [width / 3, height / 3 * 2], xWidth)
    # bottom middle
    if agentMove == (2, 1):
        pygame.draw.line(screen, xColor, [width / 3, height / 3 * 2], [width / 3 * 2, height], xWidth)
        pygame.draw.line(screen, xColor, [width / 3, height], [width / 3 * 2, height / 3 * 2], xWidth)
    # bottom right corner
    if agentMove == (2, 2):
        pygame.draw.line(screen, xColor, [width / 3 * 2, height / 3 * 2], [width, height], xWidth)
        pygame.draw.line(screen, xColor, [width / 3 * 2, height], [width, height / 3 * 2], xWidth)

if __name__ == '__main__':
    # pygame and window initialization
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

    # update screen
    pygame.display.flip()

    # set up game and agent
    print('Starting tic-tac-toe game...')
    game = TicTacToe()
    pruneIn = input("Prune? ")
    if pruneIn.lower() == "yes":
        prune = True
    else:
        prune = False
    depth = int(input("Depth? "))
    agent = Minimax(game, depth, prune)
    #game.printBoard()


    # agent goes first
    promptAgentAndMakeMove()
    gameOver = game.isTerminal()

    # update screen
    pygame.display.flip()



    # game loop
    gameOver = False
    while not gameOver:
        pos = (-1, -1)
        # get human input and process moves
        event = pygame.event.wait()
        # user quits game
        if event.type == pygame.QUIT:
            print("User ended game.")
            gameOver = True
        # user makes move
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

        # user made a move
        if pos != (-1, -1):
            promptUserAndMakeMove(pos)
            gameOver = game.isTerminal()
            # update screen
            pygame.display.flip()
            if gameOver:
                break

            # agent makes move
            promptAgentAndMakeMove()
            gameOver = game.isTerminal()

            # update screen
            pygame.display.flip()
            #game.printBoard()

        # frames per second = 24
        clock.tick(24)

    sleep(1)

    screen.fill(BLACK)

    # print winner
    score = game.scoreGame()
    font = pygame.font.SysFont('Calibri', 30, True, False)
    text = ""
    # tie
    if score == 0:
        text = font.render("TIE", True, WHITE)
    # ai wins
    elif score == 1:
        text = font.render("You lose, AI wins", True, WHITE)
    # human wins
    else:
        text = font.render("You win, AI loses", True, WHITE)
    screen.blit(text, [width / 3 + width / 12, height / 2])

    # update screen
    pygame.display.flip()
    sleep(1.5)

    # end game
    pygame.quit()

    print('Starting Checkers game...')
    game = Checkers()
    agent = Minimax(game, 3, False)

    print('Program terminated')