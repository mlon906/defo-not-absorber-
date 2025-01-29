from pygame_functions import *
import math, random, time, pickle



# to implement biomes later on 
thebackground[["black",standard]]

screenSize(1000,1000)
setBackgroundColour(thebackground[0][0])


class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, 0, self.size/100)
        showSprite(self.sprite)


setAutoUpdate(False)
c1 = Creature(random.randint(0,1000),random.randint(0,1000), "New Piskel-2.png (1).png", random.randint(10,100)) 

updateDisplay()
        
endWait()
