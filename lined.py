"""2D Graphics renderer for Numworks python programs."""
import kandinsky as kd


get_pixel=kd.get_pixel
set_pixel=kd.set_pixel
draw_string=kd.draw_string
draw_rect=kd.fill_rect
srgb=kd.color

screenx = 320
screeny = 222

def bresenham(x0,y0,x1,y1):
  line=list()
  if x0<x1:
    if y0<y1:
      y1+=3
    x1+=1
    for x in range(x0,x1):
      y=int(y0+((y1-y0)/(x1-x0))*(x-x0))
      line.append((x,y))
  elif x0>x1:
    line.append((x0,y0))
    if y0>y1:
      y0+=3
    x0+=1
    for x in range(x1,x0):
      y=int(y1+((y0-y1)/(x0-x1))*(x-x1))
      line.append((x,y))
  else:
    if y0<y1:
      y1+=1
      for y in range(y0,y1):
        line.append((x0,y))
    elif y0>y1:
      y0+=1
      for y in range(y1,y0):
        line.append((x0,y))
    else:
      line.append((x0,y0))
  return line

def draw_line(x0,y0,x1,y1,color="#000000"):
  for pixel in bresenham(x0,y0,x1,y1):
    set_pixel(pixel[0],pixel[1],color)

def rect_line(x0,y0,x1,y1,width,height,color="#000000"):
  for pixel in bresenham(x0,y0,x1,y1):
    draw_rect(pixel[0],pixel[1],width,height,color)

def draw_box(x,y,width,height,color):
  draw_rect(x,y,1,height,color)
  draw_rect(x,y,width,1,color)
  draw_rect(x+width,y,1,height,color)
  draw_rect(x,y+height,width,1,color)

def bresenham(a,b,c,d):
  line = list()
  m=max(abs(c-a),abs(d-b))
  for i in range(0,m,(m>0)*2-1): line.append((a+(c-a)*i//m,b+(d-b)*i//m))
  return line

rect_line(50,50,55,200,5,5,"purple")
draw_rect(100,100,2,2,"black")
draw_rect(100+(16*5),100+(6*5),2,2,"black")
draw_line(100,100,100+(16*5),100+(6*5),"yellow")
rect_line(100,100,100+(16*5),100+(6*5),1,1,"orange")
