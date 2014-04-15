import pygame, sys
import random
import math
import brain_dna
from pygame.locals import *

#CHEESE CLASS
""" Cheese will spawn in a random location based on timer. """
class Cheese:
    def __init__(self):
        self.x = randint(0,800)
        self.y = randint(0,600)

#MOUSE CLASS
""" Mice will spawn in random locations based on breeding.
    15 units; 2 unit breeding delay. """
class Mouse:
    def __init__(self):
        self.x = randint(0,800);
        self.y = randint(0,600);
        self.velocity = 15

#CAT CLASS
""" Mice will spawn in random locations based on breeding.
    10 units; 4 unit breeding delay. """
class Cat:
    def __init__(self):
        self.x = randint(0,800);
        self.y = randint(0,600);
        self.velocity = 10


pygame.init()

#Running the fame at 30 FPS
FPS = 30
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((800,600), 0, 32)

BLACK = (0,0,0)

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
    for i in range(2):
        allCats.append(Cat())

    #game loop
    while (len(allMice) != 0 and len(allCats) != 0):
        #update state

        #handle events
        
        #display
        if (do_display):
            #background work
            display.fill(BLACK)

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
