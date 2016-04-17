# imports modules for pygame, sys, random, time
import pygame, sys
# imports all constants for the pygame module so they can be called in game
# from pygame.locals import *
# must be called after importing pygame module and before calling any other pygame functions - runs through initialization steps for the game
def main():

    pygame.init()
    #set up window next - use display module that is inside pygame module, this sets up window that will display output from game based on user input on certain events - here we will see text images and graphics
    gameWindow = pygame.display.set_mode((1000, 1000)) #first arg is width x height in pixels of window - creates a pygame.Surface object which has its own methods
    pygame.display.set_caption('my first pygame')

    # specify colors you'll use using RGB values, a tuple with 3 arguments
    AQUA = (0, 204, 204)
    WHITE = (255, 255, 255)
    TAN = (219, 206, 160)
    PURPLE = (135, 72, 133)

    kitten = pygame.image.load("kitten.png")

    class KittenSprite:
        def __init__(self,img):
            self.image = img
            self.posn = (100, 100)

        def moveUp(self):
            (x, y) = self.posn
            new_y_posn = y - 10
            self.posn = (x, new_y_posn)

        def moveDown(self):
            (x, y) = self.posn
            new_y_posn = y + 10
            self.posn = (x, new_y_posn)

        def moveRight(self):
            (x, y) = self.posn
            new_x_posn = x + 10
            self.posn = (new_x_posn, y)

        def moveLeft(self):
            (x, y) = self.posn
            new_x_posn = x - 10
            self.posn = (new_x_posn, y)

        def draw(self,game_window):
            game_window.blit(self.image, self.posn)

    kittenPlayer = KittenSprite(kitten)

    # specify font using pygame.font
    gameFont = pygame.font.SysFont('noteworthy', 48) # font type, font size
    text = gameFont.render('my first pygame', True, PURPLE)
    textRect = text.get_rect()
    textRect.centerx = gameWindow.get_rect().centerx

    while True:
        event = pygame.event.poll() #listen for all events
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYUP:
            key = event.dict["key"]
            if key == 273:
                kittenPlayer.moveUp()
            elif key == 275:
                kittenPlayer.moveRight()
            elif key == 274:
                kittenPlayer.moveDown()
            elif key == 276:
                kittenPlayer.moveLeft()

    # fill background color for window
        gameWindow.fill(WHITE)
        kittenPlayer.draw(gameWindow)


    # draw text on game window
        gameWindow.blit(text, textRect) # copy pixels from one area in memory to another
        pygame.display.flip()
    pygame.quit()



main()