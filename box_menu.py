#!/usr/bin/python3
"""Boxes UI testing playground"""
from boxes import *
import time

#Usefull functions
def flyingBoxLaunch():
  import flying_box
  flying_box.main()

def rainbowLaunch():
  import rainbow
  rainbow.main()

def raycastingLauch():
  import raycasting
  raycasting.main()

#initialsing a UI box
box = Box()

#creating buttons in the box
buttonFlyingBox = Button(box, 'Flying Box', flyingBoxLaunch)
buttonRaibow = Button(box, 'Rainbow', rainbowLaunch)
buttonRaycasting = Button(box,'Raycasting', raycastingLauch)
buttonQuit = Button(box, "Quit", box.stop)

#packing buttons in the box
buttonFlyingBox.pack()
buttonRaibow.pack()
buttonRaycasting.pack()
buttonQuit.pack()

#rendering the box
def background():
  red=-111
  for pixely in range(screeny):
    draw_rect(0,pixely,screenx,1,srgb(int(abs(red)),0,0))
    red+=1
box.renderBackground = background

print("box.mainLoop()")
box.mainLoop()
