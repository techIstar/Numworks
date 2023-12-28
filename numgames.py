"""Python library for Numworks python games"""
from ion import *
from lined import *
import time


#Objects
class Object:
  instances=list()
  def __init__(self,posx=0,posy=0,width=16,height=16,color='#000000'):
    Object.instances.append(self)
    self.posx = posx
    self.posy = posy
    self.width = width
    self.height = height
    self.color = color

class Particle(Object):
  instances=list()
  def __init__(self,posx=0,posy=0,width=16,height=16,color='#000000',lifetime=16):
    super().__init__(posx,posy,width,height,color)
    Particle.instances.append(self)
    self._lifetime=lifetime
    fill_rect(self.posx,self.posy,self.width,self.height,self.color)

  def __del__(self):
    print("hopefully deleted")
    fill_rect(self.posx,self.posy,self.width,self.height,backg_c)
    del self

#  @property
#  def lifetime(self):
#    return self._lifetime
#  @lifetime.setter
#  def lifetime(self,new_value):
#    if new_value < 0:
#      del self
#    else:
#      self._lifetime = new_value

class Solid(Object):
  instances=list()
  def __init__(self,posx=0,posy=0,width=16,height=16,color:str='#000000'):
    super().__init__(posx,posy,width,height,color)
    Solid.instances.append(self)
    self.hitbx=width
    self.hitby=height

class Animate(Object):
  instances=list()
  def __init__(self,posx=0,posy=0,vectx=0,vecty=0,speedx=1,speedy=2,width=16,height=16,color='#000000',trail_c=None):
    super().__init__(posx,posy,width,height,color)
    Animate.instances.append(self)
    self.vectx = vectx
    self.speedx = speedx
    self.vecty = vecty
    self.speedy = speedy
    self.trail_c = color if trail_c is None else trail_c

  def move(self,x,y):
    old_x=self.posx
    old_y=self.posy
    if self.posx+x >= 0 and self.posx+x <= screenx-self.width and x!=0:
      self.posx += x
    else:
      if self.posx+x < 0:
        self.posx = 0
      elif self.posx+x > screenx-self.width:
        self.posx = screenx-self.width
      self.vectx = -self.vectx*2 if self.vectx == 1 else int(-self.vectx*0.75)

    if self.posy+y >= 0 and self.posy+y <= screeny-self.height and y!=0:
      self.posy += y
    else:
      if y < 0:
        self.posy = 0
      elif y > 0:
        self.posy = screeny-self.height
      self.vecty = -self.vecty*2 if abs(self.vecty) == 1 else int(-self.vecty*0.75)

#    trail = bresenham(old_x,old_y,self.posx,self.posy)
#    for pixel in trail:
#      Particle(pixel[0],pixel[1],self.width,self.height,self.trail_c)
    rect_line(old_x,old_y,self.posx,self.posy,self.width,self.height,self.trail_c)
    draw_rect(self.posx,self.posy,self.width,self.height,self.color)


#TODO redrawing and graphic buffer


#Functions
def at(key,func,param1):
  if keydown(key):
    func(param)


#loop
def main_loop(delay):
  run=True
  while run:
    for particle_instance in Particle.instances:
      particle_instance.lifetime -= 1

    time.sleep(delay)


#Usefull
t0 = time.monotonic()
def dt():
  return time.monotonic()-t0
backg_c="#000000"
delay=0.03

#debugging

