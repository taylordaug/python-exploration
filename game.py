import pygame, sys, random, time
from pygame.locals import *
from random import randint

class Player:
    x = 0
    y = 0
    direction = 0
    step = 10
    score_count = 0


    def __init__(self):
        self.image = pygame.image.load("hippo.jpg")
        self.x = 500
        self.y = 300

    def moveUp(self):
        self.direction = 0

    def moveDown(self):
        self.direction = 1

    def moveRight(self):
        self.direction = 2

    def moveLeft(self):
        self.direction = 3

    def update(self):
        if self.direction == 0:
            self.y = self.y - self.step
        elif self.direction == 1:
            self.y = self.y + self.step
        elif self.direction == 2:
            self.x = self.x + self.step
        elif self.direction == 3:
            self.x = self.x - self.step


    def draw(self,game_window):
        game_window.blit(self.image, (self.x, self.y))

class Fruit:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.img = pygame.image.load("pineapple.png")
        self.x = x
        self.y = y

    def draw(self,game_window):
        game_window.blit(self.img, (self.x, self.y))


class Game:
    def isCollision(self,x1,y1,x2,y2, playerSize):
        if x1 == x2 + playerSize and y1 == y2 + playerSize:
            return True


class App:
    player = 0
    fruit = 0

    def __init__(self):
        self._running = True
        self.game = Game()
        self.player = Player()
        self.fruit = Fruit(300, 300)

    def on_init(self):
        pygame.init()
        self.AQUA = (0, 204, 204)
        self.WHITE = (255, 255, 255)
        self.TAN = (219, 206, 160)
        self.PURPLE = (135, 72, 133)
        self.gameWindow = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption('hungry hungry hippos')
        self.gameFont = pygame.font.SysFont('arialblack', 36) # font type, font size
        self.text = self.gameFont.render('hungry hungry hippos', True, self.PURPLE)
        self.score = self.player.score_count
        self.scoreboard = self.gameFont.render("score: %s" % (self.score), True, self.PURPLE)
        self.scoreRect = self.scoreboard.get_rect()
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.gameWindow.get_rect().centerx

    def on_loop(self):
        self.player.update()

        self.score = self.player.score_count


        if self.game.isCollision(self.fruit.x,self.fruit.y,self.player.x,self.player.y, 20):
             self.fruit.x = randint(1,70) * 10
             self.fruit.y = randint(1,70) * 10
             self.fruit.posn = (self.fruit.x, self.fruit.y)

    def on_render(self):
        self.gameWindow.fill(self.WHITE)
        self.player.draw(self.gameWindow)
        self.fruit.draw(self.gameWindow)
        self.gameWindow.blit(self.text, self.textRect)
        self.gameWindow.blit(self.scoreboard, self.scoreRect)
        pygame.display.flip()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                self._running = False
                break

            if event.type == pygame.KEYUP:
                print self.fruit.x
                print self.fruit.y
                key = event.dict["key"]
                if key == 273:
                    self.player.moveUp()
                elif key == 275:
                    self.player.moveRight()
                elif key == 274:
                    self.player.moveDown()
                elif key == 276:
                    self.player.moveLeft()

            self.on_loop()
            self.on_render()

            time.sleep (80.0 / 1000.0);

        pygame.quit()



playGame = App()
playGame.on_execute()
