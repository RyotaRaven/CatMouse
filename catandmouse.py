import pygame, sys
import random
import math
import brain_dna
from pygame.locals import *

#CHEESE CLASS
""" Cheese will spawn in a random location based on timer. """
class Cheese:
    def __init__(self):
        self.x = random.uniform(0,800)
        self.y = random.uniform(0,600)

#MOUSE CLASS
""" Mice will spawn in random locations based on breeding.
    15 units; 2 unit breeding delay. """
class Mouse:
    def __init__(self):
        self.x = random.uniform(0,800)
        self.y = random.uniform(0,600)
        self.velocity = 15
        self.life=100 #lifevalue (size?)
        self.canBreed=True
        self.hunger=50 #idk how big to make the hunger timer

#CAT CLASS
""" Mice will spawn in random locations based on breeding.
    10 units; 4 unit breeding delay. """
class Cat:
    def __init__(self):
        self.x = random.uniform(0,800)
        self.y = random.uniform(0,600)
        self.velocity = 10
        self.life=100 #lifevalue (size?)
        self.hunger=50 #idk how big to make the hunger

pygame.init()

#Running the fame at 30 FPS
FPS = 30
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((891,880), 0, 32)

BLACK = (0,0,0)

def game_function(ann, do_display):
    random.seed(0)
    mouse= pygame.image.load("Mouse.png")
    mouse.convert()
    cat= pygame.image.load("Cat.png")
    cat.convert()
    cheese= pygame.image.load("Cheese.png")
    cheese.convert()
    floor= pygame.image.load("Floor.png")
    floor.convert()
    banner= pygame.image.load("TK.png")

    #define game state
    allCheese = []
    allMice = []
    allCats = []

    #initalizing starting cheese
    for i in range (3):
        allCheese.append(Cheese()) #start with three cheese

    #initalizing starting mice
    for i in range (3):
        allMice.append(Mouse()) #start with three mice

    #initalizing starting cheese
    for i in range(2):
        allCats.append(Cat()) #start with three cats

    #game loop
    while (len(allMice) != 0 and len(allCats) != 0):
        #update state

        #handle events
        
        #display
        if (do_display):
            #background work
            display.fill(BLACK)
            display.blit(floor, (0,280))
            display.blit(banner,(0,0))
            

            #draw cheeses
            for i in range (len(allCheese)):
                x=allCheese[i].x
                y=allCheese[i].y
                display.blit(cheese, (x,y))
                

            #draw mice
            for i in range (len(allMice)):
                x=allMice[i].x
                y=allMice[i].y
                display.blit(mouse, (x,y))

            #draw cats
            for i in range (len(allCats)):
                x=allCats[i].x
                y=allCats[i].y
                display.blit(cat, (x,y))
            
            pygame.display.flip() #because of using blit
            pygame.display.update()
            FPSCLOCK.tick(FPS)

        #need to figure out how to return
        #scores for both cats and mice?
    return 0

if (__name__ == '__main__'):
        from brain_dna import neuron
        ann = neuron()
        print game_function(ann, True)
        pygame.quit()
        sys.exit()
