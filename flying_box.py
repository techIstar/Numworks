import numgames as ng
import time
import math

#Usefull constants and variables
center = (160,111)
g = 3.14

#Main Loop
def main():
  gameover=False
  gameovers=0

  if blue: ng.draw_rect(0,0,ng.screenx,ng.screeny,"#5599ff")
  ng.draw_rect(box.posx,box.posy,box.width,box.height,box.color)
  while True:
    if stats:
      ng.draw_string("x:{}|y:{} \nx>{}|y>{}|v:{} ".format(box.posx,box.posy,box.vectx,box.vecty,round(math.sqrt(box.vectx**2+box.vecty**2),3)),0,0)
    #at(ion.KEY_DOWN,box.move,(0,5))

    #Controls
    if ng.keydown(ng.KEY_BACKSPACE):
      break
    if ng.keydown(ng.KEY_UP):
      box.vecty -= box.speedy
    if ng.keydown(ng.KEY_DOWN):
      box.vecty += box.speedy
    if ng.keydown(ng.KEY_LEFT):
      box.vectx -= box.speedx
    if ng.keydown(ng.KEY_RIGHT):
      box.vectx += box.speedx

    #gravity
#    g_vx = 160 - box.posx
#    g_vy = 111 - box.posy
#   (box.posx,box.posy,g_vx+box.posx,g_vy+box.posy,'black')
#    ng.draw_line(box.posx,box.posy,g_vx+box.posx,0*(g_vy+box.posy),'black')

#    box.vecty += 1

    if ng.keydown(ng.KEY_TOOLBOX):
      box.vectx = 0
      box.vecty = 0
      box.posx=160
      box.posy=111
      if blue: ng.draw_rect(0,0,ng.screenx,ng.screeny,"#5599ff")
      gameover=False

    #rainbow
    if rainbow_trail:
      rainbow_r = abs(math.sin(time.monotonic()+1.047))*255
      rainbow_g = abs(math.sin(time.monotonic()+2.094))*255
      rainbow_b = abs(math.sin(time.monotonic()))*255
      box.trail_c = ng.srgb(rainbow_r,rainbow_g,rainbow_b)

    box.vecty += 1

    #moving the box
    box.move(box.vectx,box.vecty)

#    for particle in ng.Particle.instances:
#      particle.lifetime -= 1

    if not gameover==False and ( box.vectx>50 or box.vecty>50 ):
      gameover=True
      gameovers+=1

    if gameover:
      ng.draw_string("Sale Victime",100,100)

    time.sleep(delay)

#Initialisation
delay = 0.012
ng.backg_c = "#ffffff"
w = 16
12
h = 16
box = ng.Animate(vectx=3,vecty=2,posx=160,posy=111,width=w,height=h,speedx=1,speedy=2,trail_c='white')
blue = 0
stats = 0
rainbow_trail = 1
