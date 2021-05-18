import pygame
import random
import sys
import math
import numpy as np

SQUARE_SIZE = 2
BLACK_SQUARE= (0,0,0)
WHITE_SQUARE = [255,255,255]
BACKGROUND_COLOR = [20, 20,30]
RED_COLOR = [250,70,70]
YELLOW_COLOR = [240,240,100]
BLUE_COLOR = [100,100,240]
GREEN_COLOR = [100,250,100]
simulationTime = 1
pygame.init() 
screen = pygame.display.set_mode([1728,960])
screen.fill(BACKGROUND_COLOR)

class Cell():

        def __init__(self,startPosX, startPosY):
                
                self.positionX = startPosX
                self.positionY = startPosY
                self.iterations = 0
                self.color = BLACK_SQUARE

         
        def Instantiate(self, x, y):
                
                pygame.draw.rect(screen, self.color,(x,y,SQUARE_SIZE, SQUARE_SIZE))     

        def Move(self, newPosX, newPosY):

                self.positionX = self.positionX + newPosX
                self.positionY = self.positionY + newPosY 
                self.Instantiate(self.positionX, self.positionY)

        def NewSequence(self, position):                
        
                if (position % 2 == 0):
                        
                        position = position/2

                else:
                
                        position = 2*position*position - position

                return position

        
        def Collatz(self, position):
                
         
                 
                if (position % 2 == 0):
                
                        position = position/2
                        self.color = GREEN_COLOR
                         

                else:
        
                        position = position * 3 + 1
                        self.color = RED_COLOR
                 

                self.iterations += 1

                if(position % 13 == 0):
                        self.color = BLUE_COLOR
                if (position % 33 == 0):
                        
                        self.color = YELLOW_COLOR
                        self.color = [((self.color[0] + YELLOW_COLOR[0])/2)%255,((self.color[1] + YELLOW_COLOR[1])/2)%255,((self.color[2] + YELLOW_COLOR[2])/2)%255]

                return position 

        def MoveCollatz(self):
 
                self.positionX = self.Collatz(self.positionX)
                self.positionY = self.Collatz(self.positionY)

                 
  
                self.Instantiate(self.positionX, self.positionY)

 

        
        def GetPosition(self):
                
                posArray = [self.positionX, self.positionY]
                
                return posArray 
        


MAX_CELLS = 100000
def CellUpdate():
        
        fiztgerald = [None] * MAX_CELLS
        


        for i in range (0, MAX_CELLS):
                collatzN = random.randint(0,1000)
                collatzY = random.randint(0,1000)
                fiztgerald[i] = Cell (collatzN, collatzY)

        running = True  
        while running: 
                 
                pygame.display.flip()
         
                if (pygame.time.delay(simulationTime)):
                        screen.fill(BACKGROUND_COLOR)

 
                
                for i in range(0,MAX_CELLS): 

                        fiztgerald[i].MoveCollatz() 
 
 

                for event in  pygame.event.get():

                        if event.type == pygame.QUIT:
                                running = False 

 

def main():  
        
        CellUpdate()
 
        
 
main()
