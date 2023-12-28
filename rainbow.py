from kandinsky import fill_rect, color
from ion import *
from time import *
from math import sin


def main(_rb_speed = 1):
  rb_speed = _rb_speed

  while True:
    rainbow_r = abs(sin(monotonic()*rb_speed+1.047))*255
    rainbow_g = abs(sin(monotonic()*rb_speed+2.094))*255
    rainbow_b = abs(sin(monotonic()*rb_speed))*255

    fill_rect(0,0,320,222,color(rainbow_r,rainbow_g,rainbow_b))

    if keydown(KEY_BACKSPACE):
      break
