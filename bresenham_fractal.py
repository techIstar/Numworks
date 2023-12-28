from lined import *
import time, math

def bf(x=160,y=111,r=0,e=0):
  centerx = x
  centery = y

  if r:
    for pixel in range(screenx):
      r_color=srgb(abs(math.sin(time.monotonic()+1.047))*255,abs(math.sin(time.monotonic()+2.094))*255,abs(math.sin(time.monotonic()))*255)
      draw_line(pixel,0,pixel,222,r_color)

  for pixel in range(-60,screenx+60):
    draw_line(pixel,222+1,centerx,centery,'black')

  if e:
    while True:
      pass

"""
  for pixel in range(screeny):
    draw_line(320,pixel,centerx,centery,'black')
  for pixel in range(screenx):
    draw_line(pixel,0,centerx,centery,'black')
  for pixel in range(screeny):
    draw_line(0,pixel,centerx,centery,'black')
"""

print("bf(y=0)")
bf(y=0)