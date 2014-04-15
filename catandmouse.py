import pygame, sys
import random
import math
import brain_dna
from pygame.locals import *

#CHEESE CLASS
class Cheese:
    def __init__(self):
        self.x = randint(0,800)
        self.y = randint(0,600)

#MOUSE CLASS
class Mouse:
    def __init__(self):
        self.x = randint(0,800);
        self.y = randint(0,600);

#CAT CLASS
class Cat:
    def __init__(self):
        self.x = randint(0,800);
        self.y = randint(0,600);


pygame.init()

#Running the fame at 30 FPS
FPS = 30
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((800,600), 0, 32)

BLACK = (0,0,0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (192, 192, 192)
BROWN = (205, 133, 63)

def game_function(ann, do_display):
    random.seed(0)

    #define game state
    allCheese = []
    allMice = []
    allCats = []

    #initalizing starting cheese
    for i in range (3):
        allCheese.append(Cheese())

    #initalizing starting mice
    for i in range (3):
        allMice.append(Mouse())

    #initalizing starting cheese
    for i in range(3):
        allCats.append(Cat())

    #game loop
    while (len(allMice) != 0 and len(allCats) != 0):
        #update state

        #handle events
        
        #display
        if (do_display):
            #background work
            display.fill(BLACK)

            #Squares should be 50 x 50 (maybe less)
            for row in range (800/50):
                for col in range (600/50):
                    tile = pygame.Rect(row, col, 50, 50)
                    pygame.draw.rect(display,WHITE, tile, 0)

            #draw cheeses

            #draw mice

            #draw cats


            pygame.display.update()
            FPSCLOCK.tick(FPS)

        #need to figure out how to return
        #scores for both cats and mice?
        return null

    if (__name__ == '__main__'):
        from brain_dna import neuron
        ann = neuron()
        print game_function(ann, True)
        pygame.quit()
        sys.exit()
