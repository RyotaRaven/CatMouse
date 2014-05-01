import pygame, sys
import random
import math
import brain_dna
from pygame.locals import *

#CHEESE CLASS
""" Cheese will spawn in a random location based on timer. """
class Cheese:
    def __init__(self):
        self.x = random.randrange(0,800)
        self.y = random.randrange(300,880)

#MOUSE CLASS
""" Mice will spawn in random locations based on breeding.
    15 units; 2 unit breeding delay. """
class Mouse:
    def __init__(self):
        self.x = random.randrange(0,800)
        self.y = random.randrange(300,880)
        self.velocity = 15
        self.life=100 #lifevalue (si5ze?)
        self.canBreed=True
        self.hunger=50 #idk how big to make the hunger timer
        self.score=0
        

#CAT CLASS
""" Mice will spawn in random locations based on breeding.
    10 units; 4 unit breeding delay. """
class Cat:
    def __init__(self):
        self.x = random.randrange(0,800)
        self.y = random.randrange(300,880)
        self.velocity = 10
        self.life=100 #lifevalue (size?)
        self.hunger=50 #idk how big to make the hunger

pygame.init()

#Running the fame at 30 FPS
FPS = 20
FPSCLOCK = pygame.time.Clock()

#set up display
display = pygame.display.set_mode((891,880), 0, 32)

BLACK = (0,0,0)


def game_function(ann, do_display):
    random.seed()
    mouse= pygame.image.load("Mouse.png")
    mouse.convert()
    cat= pygame.image.load("Cat.png")
    cat.convert()
    cheese= pygame.image.load("Cheese.png")
    cheese.convert()
    floor= pygame.image.load("Floor.png")
    floor.convert()
    banner= pygame.image.load("TK.png")

    cheeseCount=0

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
        cheeseCount+=1

        if(cheeseCount%50==0):
            allCheese.append(Cheese())
        
        mouseInputX=[] #goes to cat
        mouseInputY=[]
        catInputX=[] #goes to mouse
        catInputY=[]
        cheeseInputX=[] #goes to both
        cheeseInputY=[]

        #setting up ANN inputs
        for i in range (len(allCats)):
            for x in range(len(allMice)):
                mouseInputX.append(allCats[i].x-allMice[x].x)
                mouseInputY.append(allCats[i].y-allMice[x].y)
        for i in range (len(allMice)):
            for x in range(len(allCheese)):
                cheeseInputX.append(allMice[i].x-allCheese[x].x)
                cheeseInputY.append(allMice[i].y-allCheese[x].y)
        for i in range (len(allMice)):
            for x in range(len(allCats)):
                catInputX.append(allMice[i].x-allCats[x].x)
                catInputY.append(allMice[i].y-allCats[x].y)
        isMouse=0
        isCat=1
    
        #eating  
        for m in list (allMice):
            mouseRect=Rect(m.x,m.y,40,33)
            for c in list (allCats):
                catRect= Rect(c.x,c.y,40,33)
                if(mouseRect.colliderect(catRect)):
                    allMice.remove(m)
                    
                    
        for m in list (allMice):
            mouseRect=Rect(m.x,m.y,40,33)
            for ch in list (allCheese):
                cheeseRect= Rect(ch.x,ch.y,40,33)
                if(mouseRect.colliderect(cheeseRect)):
                    allCheese.remove(ch)


        for i in range (len(allMice)):
            if(allMice[i].x<=0):
                allMice[i].x=0
        for i in range (len(allMice)):
            if(allMice[i].x>=760):
                allMice[i].x=760
        for i in range (len(allMice)):
            if(allMice[i].y<=300):
                allMice[i].y=300
        for i in range (len(allMice)):
            if(allMice[i].y>=850):
                allMice[i].y=850
                
        for i in range (len(allCats)):
            if(allCats[i].x<=0):
                allCats[i].x=0
        for i in range (len(allCats)):
            if(allCats[i].x>=760):
                allCats[i].x=760
        for i in range (len(allCats)):
            if(allCats[i].y<=300):
                allCats[i].y=300
        for i in range (len(allCats)):
            if(allCats[i].y>=850):
                allCats[i].y=850
            
                
        #handle events
        
        for i in range (len(allMice)):
            MmoveX = ann.run(catInputX,cheeseInputX, isMouse)
            if(MmoveX < 0):
                allMice[i].x-=allMice[i].velocity
            elif(MmoveX > 0):
                allMice[i].x+=allMice[i].velocity
            else:
                allMice[i].x = allMice[i].x
                #mouse x does not change

        for i in range (len(allMice)):
            MmoveY = ann.run(catInputY,cheeseInputY, isMouse)
            if(MmoveX < 0):
                allMice[i].y-=allMice[i].velocity
            elif(MmoveX > 0):
                allMice[i].y+=allMice[i].velocity
            else:
                allMice[i].y = allMice[i].y
                #mouse y does not change


        #if (CmoveX < 0):
            #cat moves left
        #elif (CmoveX > 0):
            #cat moves right
        #else:
            #cat x does not change

        #if (CmoveY < 0):
            #cat moves down
        #elif (CmoveY > 0):
            #cat moves up
        #else:
            #cat y does not change
        
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
