import pygame
import sudoku
import time

#Initialize our game!
pygame.init()

#Constants
WINDOW_WIDTH = 600
WINDOW_HEIGTH = 600
SCREEN_COLOR = (250, 250, 200)
LINE_COLOR = (200, 200, 200)
BORDER_COLOR = (0, 0, 0)
FREE_DISTANCE_X = 80
FREE_DISTANCE_Y = 80
NUM_BLOCKS = 9
CUBE_SIDE = (WINDOW_WIDTH - 2*FREE_DISTANCE_X) // NUM_BLOCKS
FONT_SIZE = 30
OPTIONS_TEXT_SIZE = 14
NUMBER_COLOR = BORDER_COLOR
TEXT_COLOR = BORDER_COLOR
GUESS_COLOR = (255, 0, 0)
CHOSEN_CUBE_COLOR = (255, 0, 0)
FREE_DISTANCE_TEXT = 10

#Font for numbers and text
font = pygame.font.SysFont('arial', FONT_SIZE)
text_font = pygame.font.SysFont('arial', OPTIONS_TEXT_SIZE)

#Create canvas
screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGTH))

#Icon and title
icon = pygame.image.load("brainstorm.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Saba's sudoku")

#Create sudoku board and its identical board that we will solve
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

solved_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Creates empty sudoku board for a player to fill with guesses
guess_board = [[0 for _ in range(NUM_BLOCKS)] for _ in range(NUM_BLOCKS)]

#Solves our initial board with the function of the previous class

sudoku.solve_sud(solved_board)

#Draws the board
def drawBoard():
    for i in range(NUM_BLOCKS + 1):
        if(i % 3 != 0):
            color = LINE_COLOR
        else:
            color = BORDER_COLOR
        pygame.draw.line(screen, color, (FREE_DISTANCE_X + i*CUBE_SIDE, FREE_DISTANCE_Y), (FREE_DISTANCE_X + i*CUBE_SIDE, FREE_DISTANCE_Y + NUM_BLOCKS*CUBE_SIDE))
        pygame.draw.line(screen, color, (FREE_DISTANCE_X, FREE_DISTANCE_Y + i*CUBE_SIDE), (FREE_DISTANCE_X + NUM_BLOCKS*CUBE_SIDE, FREE_DISTANCE_Y + i*CUBE_SIDE))

#Fills the drawn board
def fillBoard(board, color):
    for i in range(NUM_BLOCKS):
        for j in range(NUM_BLOCKS):
            if(board[i][j] != 0):
                number = font.render(str(board[i][j]), True, color)
                screen.blit(number, (FREE_DISTANCE_X + (j + 0.5)*CUBE_SIDE - FONT_SIZE/4 , FREE_DISTANCE_Y + (i + 0.5)*CUBE_SIDE - FONT_SIZE/2))

#Prints text in the upper left corner
def printOptions():
    text1 = text_font.render("Press 'Enter' to check your board", True, TEXT_COLOR)
    screen.blit(text1, (FREE_DISTANCE_TEXT, FREE_DISTANCE_TEXT))
    
    text2 = text_font.render("Press 'Space' to autofill the board", True, TEXT_COLOR)
    screen.blit(text2, (FREE_DISTANCE_TEXT, FREE_DISTANCE_TEXT*3))

#Checks where the mouse was clicked and prints the guess if necessary
def handle_mouseclick(pos):
    if(pos[0] > FREE_DISTANCE_X and pos[0] < WINDOW_WIDTH - FREE_DISTANCE_X and pos[1] > FREE_DISTANCE_Y and pos[1] < WINDOW_HEIGTH - FREE_DISTANCE_Y):
        j = (pos[0] - FREE_DISTANCE_X) // CUBE_SIDE
        i = (pos[1] - FREE_DISTANCE_Y) // CUBE_SIDE
        if (board[i][j] == 0):
            handle_guess(i, j)

#Asks for the user to type input and handles this input
def handle_guess(i, j):
    #"Enter your guess" appears in the middle of screen and given cube lights up
    
    text = font.render("Enter your guess".center(20), True, NUMBER_COLOR)
    screen.blit(text, (WINDOW_WIDTH/3.5, FREE_DISTANCE_Y/2))
    screen.fill(CHOSEN_CUBE_COLOR, (FREE_DISTANCE_X + j*CUBE_SIDE, FREE_DISTANCE_Y + i*CUBE_SIDE, CUBE_SIDE, CUBE_SIDE))
    pygame.display.update()

    #This is the loop handling user's guess 
    running = True
    while running:
        for event in pygame.event.get():
            
            #User can quit this mode when he presses the mouse
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP:
                running = False

            #We check the keyboard for pressed numbers
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                     guess_board[i][j] = 1
                     
                if event.key == pygame.K_2:
                     guess_board[i][j] = 2
                     
                if event.key == pygame.K_3:
                     guess_board[i][j] = 3
                     
                if event.key == pygame.K_4:
                     guess_board[i][j] = 4
                     
                if event.key == pygame.K_5:
                     guess_board[i][j] = 5
                     
                if event.key == pygame.K_6:
                     guess_board[i][j] = 6
                     
                if event.key == pygame.K_7:
                     guess_board[i][j] = 7
                     
                if event.key == pygame.K_8:
                     guess_board[i][j] = 8

                if event.key == pygame.K_9:
                     guess_board[i][j] = 9

                running = False

#Method called when user presses 'Enter'
def handle_enter():
    for i in range(NUM_BLOCKS):
        for j in range(NUM_BLOCKS):
            if board[i][j] == 0:
                if guess_board[i][j] != solved_board[i][j]:
                    text = font.render("Your guesses are wrong".center(20), True, NUMBER_COLOR)
                    screen.blit(text, (WINDOW_WIDTH/3.5, FREE_DISTANCE_Y/2))
                    pygame.display.update()
                    time.sleep(2)
                    return False
    return True

#Method called when user presses 'Space'
def handle_space():
    for i in range(NUM_BLOCKS):
        for j in range(NUM_BLOCKS):
            if board[i][j] == 0:
                guess_board[i][j] = solved_board[i][j]

#Main game loop
running = True
while running:
    
    #Loop through all the events
    for event in pygame.event.get():

        #Handle quitting
        if event.type == pygame.QUIT:
            running = False
        
        #Handle mouse clicking
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            handle_mouseclick(pos)
        
        #Handle 'Enter' and 'Space' pressdowns
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN:
                if handle_enter():
                    text = font.render("Congratulations, you've won!".center(20), True, NUMBER_COLOR)
                    screen.blit(text, (WINDOW_WIDTH/3.5, FREE_DISTANCE_Y/2))
                    pygame.display.update()
                    time.sleep(2)
                    running = False
            
            if event.key == pygame.K_SPACE:
                handle_space()

    screen.fill(SCREEN_COLOR)
    drawBoard()
    fillBoard(board, NUMBER_COLOR)
    fillBoard(guess_board, GUESS_COLOR)
    printOptions()
    pygame.display.update()
