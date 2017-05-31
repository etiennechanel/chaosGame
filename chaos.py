#!/usr/bin/python3
# -*- coding: utf-8 -*-
#########################
#HEXA_CHAOS
#Etienne_Chanel 30/05/17
from tkinter import *
from random import randrange

# fonctions
def drawDot(x0, y0, color):
    can1.create_oval(x0, y0, x0+1, y0+1, fill=color, outline='')
    # One other dot style.
    #can1.create_line(x0,y0,x0+1,y0+1,width=1,fill=color)
    #can1.create_line(x0+1,y0,x0,y0+1,width=1,fill=color)
    
def chaos(nbDot, posDir):
    x0, y0 = 500, 500
    i = 1
    while i <= nbDot :
        c = randrange(len(posDir))
        direction = posDir[c]
        x0 =  (direction [0]+x0)/2
        y0 =  (direction [1]+y0)/2
        color = direction[2]
        drawDot(x0, y0, color)
        if i%(nbDot/10) == 0:
            print(int((i/(nbDot/100))),"%")
            can1.update()
        i = i+1
    """print ("start saving postscript image ")
    can1.update()
    can1.postscript(file="file_name.ps", colormode='color')
    print ("postscript image file save")"""
    return(print(nbDot, " dots have been displayed"))


# variables
A = [500, 100, 'cyan']
B = [900, 300, 'blue']
C = [900, 700, 'magenta']
D = [500, 900, 'red']
E = [100, 700, 'yellow']
F = [100, 300, 'green']
# Add, delete or change coordinates associate to a color.
# Use only 3 points to make some Sierpinski triangle ex below.
#posDir = [A, C, E]
posDir = [A, B, C, D, E, F]
# program
fen1 = Tk()
can1 = Canvas(fen1,bg='black',height=1000,width=1000)
can1.pack()

# choose how many dots you want to display
chaos(100000, posDir)
