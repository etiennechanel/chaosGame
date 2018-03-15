#!/usr/bin/python3
# -*- coding: utf-8 -*-
#chaosGame.py
#Etienne_Chanel 03/15/18

from tkinter import *
from random import randrange

#image file name 
name = 'chaosGame01'
#number of dots to display
dotsNumber = 100000
#display size
width = 1000
height = 800
#background color
bgColor = 'black'
#def polygon points coordinates and color
A = (0, height * 0.5, 'green')
B = (width / 4, height, 'yellow')
C = (width / 4 * 3, height, 'red')
D = (width, height * 0.5, 'magenta')
E = (width / 4 * 3,  0, 'blue')
F = (width / 4, 0, 'cyan')

polygone = (A, B, C, D, E, F)
center = (width / 2, height / 2, '')

#fonctions
def drawDot(x, y, color):
    can1.create_oval(x, y, x+2, y+2, fill=color, outline='')
    
def chaos(polygon, dotsNumber):
    x0, y0 = width / 2, height / 2
    direction = center
    color = direction[2]
    
    for i in range(dotsNumber):
        hazard = randrange(len(polygone))
        direction = polygone[hazard]
        x0 =  (direction [0]+x0)/2
        y0 =  (direction [1]+y0)/2
        color = direction[2]
        drawDot(x0, y0, color)
        
        if i%(1000) == 0:
            can1.update()
            print (i, "DOTS")
            
    #print ("tkinter is saving postscript image, ... ")
    #can1.update()
    #can1.postscript(file= name +".ps", colormode='color')
    #print (name, "has been saved")
    return(print(dotsNumber, " dots have been displayed"))


#run
fen1 = Tk()
can1 = Canvas(fen1, bg=bgColor, height=height, width=width)
can1.pack()
chaos(polygone, dotsNumber)
fen1.mainloop()
