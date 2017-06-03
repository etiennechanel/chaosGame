#!/usr/bin/python3
# -*- coding: utf-8 -*-
#chaosGame.py
#Etienne_Chanel 03/06/17
from tkinter import *
from random import randrange

#fonctions
def drawDot(x, y, color):
    can1.create_oval(x, y, x+1, y+1, fill=color, outline='') #can1.create_line(x0,y0,x0+1,y0+1,fill=color, outline='')
    #can1.create_line(x0+1,y0,x0,y0+1,fill=color, outline='')

def drawPoly(polyX, color):
    pts = []
    for i in range(len(polyX)):
        xy = polyX[i]
        pts.append(xy [0])
        pts.append(xy [1])
    can1.create_polygon(pts, fill=color, outline='') 
    can1.update()
    
def chaos(polyX, nbDot):
    x0, y0 = xWidth / 2, yHeigh / 2
    for i in range(nbDot):
        rollAdie = randrange(len(polyX))
        direction = polyX[rollAdie]
        x0 =  (direction [0]+x0)/2
        y0 =  (direction [1]+y0)/2
        color = direction[2]
        drawDot(x0, y0, color)
        if i%(nbDot/10) == 0:
            print(int((i/(nbDot/100))),"%")
            can1.update()
    """print ("start saving postscript image ")
    can1.update()
    can1.postscript(file="file_name.ps", colormode='color')
    print ("postscript image file save")"""
    return(print(nbDot, " dots have been displayed"))
    
#variables
xWidth = 600
yHeigh = 600
bgColor = 'white'
polyColor= 'black'
#each polygon point coordonates and color
A = (xWidth * 0.5, yHeigh * 0.1, 'cyan')
B = (xWidth * 0.9, yHeigh * 0.3, 'blue')
C = (xWidth * 0.9, yHeigh * 0.7, 'magenta')
D = (xWidth * 0.5, yHeigh * 0.9, 'red')
E = (xWidth * 0.1, yHeigh * 0.7, 'yellow')
F = (xWidth * 0.1, yHeigh * 0.3, 'green')
#make a polygon
polyX = (A, B, C, D, E, F) 

#program
fen1 = Tk()
can1 = Canvas(fen1, bg=bgColor, height=yHeigh, width=xWidth)
can1.pack()

drawPoly(polyX, polyColor)
chaos(polyX, 100000)

can1.update()
fen1.mainloop()
