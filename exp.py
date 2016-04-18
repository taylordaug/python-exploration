# imports modules for pygame, sys, random, time
# This Python file uses the following encoding: utf-8
import pygame, sys, random, time
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

    kitten = pygame.image.load("hippo.jpg")

    class Player:
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

        def collide(self, sprite2):
            if pygame.sprite.spritecollide(self, sprite2, True):
                self.speed[0] = -self.speed[0]
                self.speed[1] = -self.speed[1]

    class Fruit:
        def __init__(self):
            self.img = pygame.image.load("pineapple.png")
            self.posn = (10,10)

        def draw(self,game_window):
            game_window.blit(self.img, self.posn)

        # def moveFruit(self, windowSize):
        #     self.rect = self.rect.move(self.speed)
        #     if self.rect.left < 0 or self.rect.right > windowSize[0]:
        #         self.speed[0] = -self.speed[0]
        #     if self.rect.top < 0 or self.rect.bottom > windowSize[1]:
        #         self.sped[1] = -self.speed[1]

            # def collide(self, group1):
                # if pygame.sprite.spritecollide(self, group1, True):
                #     self.speed[0] = -self.speed[0]
                #     self.speed[1] = -self.speed[1]

    class Game:
        def __init__(self):
        def isCollision(self,x1,y1,x2,y2,bsize):
                if x1 >= x2 and x1 <= x2 + bsize:
                    if y1 >= y2 and y1 <= y2 + bsize:
                        return True
                return False

    player = Player(kitten)
    fruit = Fruit()



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
                player.moveUp()
            elif key == 275:
                player.moveRight()
            elif key == 274:
                player.moveDown()
            elif key == 276:
                player.moveLeft()

    # fill background color for window
        gameWindow.fill(WHITE)
        player.draw(gameWindow)
        fruit.draw(gameWindow)


    # draw text on game window
        gameWindow.blit(text, textRect) # copy pixels from one area in memory to another
        pygame.display.flip()

    pygame.quit()

main()