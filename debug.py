from numgames import *
import math


#particle = ng.Particle(25,25,16,16,'green',120)
w=16
h=16
delay=0.03
def new_A(posy=screeny-h,width=w,height=h,speedy=2):
  Animate(posy,width,height,speedy)
print("new_A()")
print("print(Animate.instances)")
