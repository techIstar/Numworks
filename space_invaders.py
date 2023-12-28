from math import *
from kandinsky import *
from ion import *
from random import *
from time import *   
from matplotlib.pyplot import *
nettoyage=monotonic()+3.5
Pause=False
b=90
l=[]
posx_plane_intro=10
fill_rect(0,0,320,230,"black")
for n in range(100): 
  set_pixel(randint(0,320),randint(0,220),(255,255,255))
draw_string("Space Invader",90,90,"green","black")
draw_string("by Gugus_BSS",90,200,"white","black")
def plane_intro():
  return [fill_rect(posx_plane_intro,50,16,5,"grey"),fill_rect(posx_plane_intro-2,50,18,3,"grey"),fill_rect(posx_plane_intro-4,45,4,4,"grey"),fill_rect(posx_plane_intro+16,51,1,3,"grey"),fill_rect(posx_plane_intro+17,52,3,1,"grey"),set_pixel(posx_plane_intro-3,50,"grey"),fill_rect(posx_plane_intro,48,2,2,"grey"),fill_rect(posx_plane_intro,49,3,1,"grey"),fill_rect(posx_plane_intro+4,52,7,1,"black"),fill_rect(posx_plane_intro+6,49,4,2,"blue"),fill_rect(posx_plane_intro-5,45,1,9,"black"),fill_rect(posx_plane_intro-4,50,1,4,"black"),fill_rect(posx_plane_intro-2,51,1,3,"black"),fill_rect(posx_plane_intro-2,53,2,2,"black")]
for x in range(320):
  posx_plane_intro+=1
  plane_intro()
  sleep(0.003)
  fill_rect(0,54,posx_plane_intro,2,"red")
pos_etoiles=[]
pos_alien=[[15,30],[40,30],[65,30],[90,30],[115,30],[140,30],[165,30],[190,30],[215,30]]
autorise=False
plane=1
j=-10
waves=0
h=0
Kill = 0
level = 0
shoot = 0
def plane1(): 
  return[fill_rect(posx-5,posy,10,2,"grey"),fill_rect(posx-1,posy-4,2,8,"grey"),fill_rect(posx-4,posy-1,8,1,"grey"),fill_rect(posx-3,posy-2,6,1,"grey"),fill_rect(posx-2,posy-3,4,2,"grey"),fill_rect(posx-1,posy-5,2,1,"green"),fill_rect(posx-1,posy-3,2,3,"blue")]
def plane2(): 
  return [fill_rect(posx-5,posy,10,2,"grey"),fill_rect(posx-1,posy-4,2,8,"grey"),fill_rect(posx-4,posy-1,8,1,"grey"),fill_rect(posx-3,posy-2,6,1,"grey"),fill_rect(posx-2,posy-3,4,2,"grey"),fill_rect(posx-1,posy-5,2,1,"grey"),fill_rect(posx-1,posy-3,2,3,"blue"),fill_rect(posx-6,posy-1,1,3,"grey"),fill_rect(posx+6,posy-1,1,3,"grey")]
def plane3():
  return [fill_rect(posx-9,posy,19,2,"blue"),fill_rect(posx-2,posy-8,5,10,"blue"),fill_rect(posx-1,posy-10,3,14,"blue"),fill_rect(posx-7,posy-1,15,1,"blue"),fill_rect(posx-6,posy-2,13,1,"blue"),fill_rect(posx-5,posy-3,11,1,"blue"),fill_rect(posx-4,posy-4,9,1,"blue"),fill_rect(posx-3,posy-5,7,1,"blue"),fill_rect(posx-9,posy-3,1,3,"grey"),fill_rect(posx+9,posy-3,1,3,"grey"),fill_rect(posx-1,posy-7,3,3,"green"),fill_rect(posx,posy-8,1,1,"green"),set_pixel(posx,posy-11,"blue")]
def alien1():
  return [fill_rect(j-4,h,10,10,(0,200,0)),fill_rect(j-6,h+2,14,8,(0,200,0)),fill_rect(j-8,h+4,18,4,(0,200,0)),fill_rect(j-10,h+6,2,6,(0,200,0)),fill_rect(j+10,h+6,2,6,(0,200,0)),fill_rect(j-6,h+10,2,2,(0,200,0)),fill_rect(j+6,h+10,2,2,(0,200,0)),fill_rect(j-4,h+12,4,2,(0,200,0)),fill_rect(j+2,h+12,4,2,(0,200,0)),fill_rect(j-6,h-2,2,2,(0,200,0)),fill_rect(j+6,h-2,2,2,(0,200,0)),fill_rect(j-4,h+4,2,2,"white"),fill_rect(j+4,h+4,2,2,"white")]
def alien3():
  return [fill_rect(j-4,h,10,10,"black"),fill_rect(j-6,h+2,14,8,"black"),fill_rect(j-8,h+4,18,4,"black"),fill_rect(j-10,h+6,2,6,"black"),fill_rect(j+10,h+6,2,6,"black"),fill_rect(j-6,h+10,2,2,"black"),fill_rect(j+6,h+10,2,2,"black"),fill_rect(j-4,h+12,4,2,"black"),fill_rect(j+2,h+12,4,2,"black"),fill_rect(j-6,h-2,2,2,"black"),fill_rect(j+6,h-2,2,2,"black"),fill_rect(j-4,h+4,2,2,"black"),fill_rect(j+4,h+4,2,2,"black")]
def alien2():
  return [fill_rect(j-4,h-2,10,2,"black"),fill_rect(j-6,h-3,14,2,"black"),fill_rect(j-10,h,6,2,"black"),fill_rect(j-10,h+2,4,2,"black"),fill_rect(j-10,h+4,2,2,"black"),fill_rect(j-4,h+10,10,2,"black"),fill_rect(j+6,h,6,2,"black"),fill_rect(j+8,h+2,4,2,"black"),fill_rect(j+10,h+4,2,2,"black")]
posx = 90
posy = 215
laser1 = 90
laser1_1=laser1
laser1_2=laser1-400
laser2 = 210
autorise_laser2_1=True
autorise_laser2_2=False
laser2_1=laser2
laser2_2=laser2
Boost=monotonic()+randint(8,20)
for x in range(80):
  pos_etoiles.append([randint(0,210),randint(0,230)],)
laser1=posx
i=0 
wave=0
a=0
record_kill=0
best_wave=0
right=True
left=True
draw_string("Space Invader",90,90,"black","black")
draw_string("Space Invader",90,30,"green","black")
draw_string("by GusGus_BBS",90,200,"black","black")
def menu(): 
  return[fill_rect(0,70,320,200,"black"),draw_string("mode:→",75,80,"white","black"),draw_string("commands:→",75,100,"white","black"),draw_string("press OK to play",70,200,"red","black"),draw_string("kill all the alien ",60,180,"green","black"),draw_string("protect our base!",60,160,"green","black")]
objectif=1
pv=10
mode=1
menu_select=1
menu()
menus=True
file=0
files=0
while not keydown(KEY_OK): 
  try: 
    files=open("space_kill.sav","r")
    file=open("space_waves.txt","r")
    record_kill=files.readline()
    best_wave=file.readline()       
  except:
    print(">failed to read the score<")
    print(">get omega to read the score!<")
  if menus==True:
    draw_string(str(record_kill),125,2,"red","black")
    draw_string("record kill:",2,2,"red","black")
    draw_string("best wave:",183,2,"pink","black")
    draw_string(str(best_wave),283,2,"pink","black")   
  if keydown(KEY_BACKSPACE):
    menu()
    menus=True
  if keydown(KEY_UP)and menu_select>1:
    menu_select-=1
  if keydown(KEY_DOWN)and menu_select<2:
    menu_select+=1
  if menu_select==2 and menus==True:
    draw_string("mode:→",75,80,"white","black")
    draw_string("commands:→",75,100)
  if keydown(KEY_RIGHT) and menu_select==2 and menus==True:
    menus=False
    fill_rect(0,70,320,200,"black")
    draw_string("press right or left to move",0,90,"white","black")
    draw_string("only in easy mode:",2,113,"white","black")
    draw_string("press ok to have a speed boost",20,136,"white","black")
    draw_string("press back_space\clear to back",0,160,"white","black")
    draw_string("capture the blue squares to have",0,183,"blue","black")
    draw_string("mysterious power...",0,203,"blue","black")
  elif menu_select==1 and menus==True:
    draw_string("commands:→",75,100,"white","black")
    draw_string("mode:→",75,80)
  if keydown(KEY_RIGHT) and menu_select==1 and menus==True:
    mode+=1
    sleep(0.2)
    if mode>3:
      mode=1
  if mode==3 and menus==True: 
    draw_string("<hardcore>",138,80,"white","black")     
    pv=1
  if mode==2 and menus==True:
    draw_string("<normal>",138,80,"white","black")
    pv=3
  if mode==1 and menus==True: 
    pv=5
    draw_string("xxxxxx",198,80,"black","black")     
    draw_string("<easy>",138,80,"white","black") 
if mode==1:
  pv=5
if mode==2:
  pv=3
if mode>3:
  pv=1
pause=False
autorise_bombe_H=False   
fill_rect(230,0,100,220,"grey")
draw_string("waves:",235,50,(0,0,0),"grey")
fill_rect(230,0,3,220,"red")
fill_rect(230,70,90,3,"red")
fill_rect(0,0,230,290,"black")
draw_string("PV:",235,180,"black","grey")
record_kill=int(record_kill)
while pv >0 :   
  if get_pixel(15,25)!=(0,200,0) and get_pixel(40,25)!=(0,200,0) and get_pixel(65,25)!=(0,200,0) and get_pixel(90,25)!=(0,200,0) and get_pixel(115,25)!=(0,200,0) and get_pixel(140,25)!=(0,200,0) and get_pixel(165,25)!=(0,200,0) and get_pixel(190,25)!=(0,200,0) and get_pixel(215,25)!=(0,200,0) and autorise==False:
    laser2_1=210
    laser2_2=210
    if plane==1:
      laser1_1=laser1
      laser1_2=laser1
    if plane>1:
      laser1_1=laser1-10
      laser1_2=laser1+10
    h=0
    if waves<6: 
      waves+=1
    wave+=1
    fill_rect(0,0,230,210,"black")
    l=[]
    for x in range(waves): 
        j=-10
        h+=25
        for i in range(9):
          j+=25
          l=l+[[j,h]]           
          alien1()   
          laser2=210
  draw_string(str(wave),300,50,"black","grey")
  draw_string(str(pv),275,180,"black","grey")
  for x in pos_etoiles:
    set_pixel(x[1],x[0],"white")
  draw_string("Kill:",235,20,"black","grey")
  draw_string(str(Kill),290,20,"black","grey")     
  if autorise == False :
    h=0
    j=15
    x=randint(0,8)
    for x in range(x):
      j+=25
    x=randint(1,waves)     
    for x in range(x):
      h+=25               
    if get_pixel(j,h)==(0,200,0) and get_pixel(j,h+27)==(0,0,0):
      time=uniform(monotonic()+0.5,monotonic()+1.5)
      autorise=True 
    else:
      autorise=False 
  if get_pixel(j,h)== (0,0,0):
    autorise=False     
  if autorise == True and monotonic()>time :
    if h <220 and get_pixel(j,h)!=(248,0,0) :     
       h+=1
       if mode==1:
         sleep(0.005)
       alien1()
       alien2()
    else:
       alien3()
       h=0
       j=15
       Kill+=1   
       autorise=False
  if h>=219 and autorise==True :
    pv-=1
    alien3()
    h=0
    draw_string(str(pv),275,180,"black","grey")
    autorise= False 
  if laser2>0: 
    if autorise_laser2_1==True: 
      laser2_1-=3
      if plane>=3:
        laser2_1-=2
      fill_rect(laser1_1,laser2_1,4,9,(248,0,0))   
    if autorise_laser2_2==True and plane>1:
      laser2_2-=3
      if plane>=3:
        laser2_2-=2
      fill_rect(laser1_2,laser2_2,4,9,(248,0,0))
    laser2-=3
    if plane>=3:
        laser2-=2
    fill_rect(laser1_1,laser2_1+9,4,9,"black") 
    fill_rect(laser1_2,laser2_2+9,4,9,"black")
  else:
    fill_rect(laser1_1,laser2_1,4,9,"black")     
    fill_rect(laser1_2,laser2_2,4,9,"black")
    laser2_1=210
    laser2_2=210
    laser2=210
    if plane>1:
      laser1_1=posx-10
      laser1_2=posx+10
    else:
      laser1_1=posx
      laser1_2=posx
    laser1=posx   
    autorise_laser2_1=True
    autorise_laser2_2=True
  if get_pixel(laser1_1,laser2_1-4)== (0,200,0):
    if plane>1: 
      fill_rect(laser1-25,laser2_1-19,25,27,"black")
    else:
      fill_rect(laser1_1-12,laser2_1-19,25,27,"black")
    fill_rect(laser1_1,laser2_1,4,9,"black")     
    Kill+=1
    laser2_1=210
    autorise_laser2_1=False       
  if get_pixel(laser1_2,laser2_2-4)== (0,200,0):
    fill_rect(laser1_2-10,laser2_2-19,27,27,"black")
    fill_rect(laser1_2,laser2_2,4,9,"black")
    Kill+=1
    laser2_2=210
    autorise_laser2_2=False
  if keydown(KEY_RIGHT) and posx < 200 and right==True:
    fill_rect(posx-10,posy-12,20,20,"black") 
    posx += 25
    right=False
  if not keydown(KEY_RIGHT):
    right=True       
  if plane==1: 
    plane1()
  elif plane==2:
    plane2()
  elif plane>=3:
    plane3()
  if keydown(KEY_SHIFT) and keydown(KEY_THREE):
    autorise_bombe_H=True
    plane=3 
  if keydown(KEY_SHIFT) and autorise_bombe_H==True:
    ih=0
    ij=0
    for i in range(200):
      if ij<100 : 
        ij+=1
      if i<113:
        ih+=1
      fill_rect(113-ih,100-ij,2*ih,2*ij,"red")
    fill_rect(0,0,234,220,"black")
    autorise_bombe_H=False 
  if keydown(KEY_LEFT) and posx > 35 and left==True:         
    fill_rect(posx-10,posy-12,20,20,"black") 
    posx -= 25
    left=False   
  if keydown(KEY_OK) and keydown(KEY_RIGHT) and mode==1:
    sleep(0.02)
    right=True
  if keydown(KEY_OK) and keydown(KEY_LEFT)and mode==1:
    sleep(0.02)
    left=True
  if not keydown(KEY_LEFT):
    left=True
  if plane==1: 
    plane1()
  elif plane==2:
    plane2()
  elif plane>=3:
    plane3()
  if not keydown(KEY_BACKSPACE)and Pause==True:
    Pause=False   
  if keydown(KEY_BACKSPACE)and pause==False and Pause== False:
    pause=True 
    while pause==True:
      draw_string("GAME",235,120,"red","grey")
      draw_string("PAUSED",235,135,"red","grey")
      if not keydown(KEY_BACKSPACE):
        Pause=True
      if keydown(KEY_BACKSPACE)and Pause==True:
        pause=False
        Pause=True   
    draw_string("XXXXXX",235,120,"grey","grey")
    draw_string("XXXXXX",235,135,"grey","grey")
    pause=False   
  if monotonic()>Boost and a<220 and plane<=3 and get_pixel(b+2,30)!=(0,200,0) and get_pixel(b-5,30)!=(0,200,0) and j!=90:
    autorise=True
    b=90
    if plane>1:
      b=102     
    fill_rect(b-4,a,7,7,"black")
    a+=1
    fill_rect(b-4,a,7,7,(56,45,190))
  elif a>219 :
    Boost=monotonic()+randint(8,30)
    a=0
    autorise=False
  if  a==215 and posx==b and plane==3:
    autorise_bombe_H=True
    draw_string("press",235,90,"black","grey")
    draw_string("shift",235,105,"black","grey")
  if a==215 and posx==b and plane<=3:
    fill_rect(b-4,a,7,7,"black")
    autorise_laser2_1=False
    autorise_laser2_2=False
    fill_rect(laser1_1,laser2_1-10,10,10,"black")
    plane+=1
    a=0
    autorise=False
    posx=102
    Boost=monotonic()+randint(8,30)   
    if plane<3: 
      fill_rect(posx-20,posy-15,40,40,"black")
      posx=102   
  if monotonic()>nettoyage and autorise==False:
    fill_rect(0,180,230,50,"black")
    nettoyage=monotonic()+3.5
fill_rect(0,0,230,220,"purple")
draw_string("GAME OVER",100,100,"green","purple")
record_kill=int(record_kill)
best_wave=int(best_wave)
if wave>8 and mode==3 or wave>=14 and mode==2 or wave>30 and mode==1:
  draw_string("You win!",100,120,"yellow","black")
else:
  draw_string("You lost",100,120,"red","purple")
try:
  if Kill>record_kill:
    files=open("space_kill.sav","w")
    files.truncate(0)
    files.write(str(Kill))
    files.close()
  if wave>best_wave: 
    file=open("space_waves.txt","w")
    file.truncate(0)
    file.write(str(wave))
    file.close()
  print(">score saved !")
except:
  print(">failed to save the score...<")
  print(">get omega to read the score<")
"""
!Space invaders!
dedicace a la classe 2nd herodote de la sauque
ecris par Gugus_BSS
mon discord:Gugus_BSS#6600
"""