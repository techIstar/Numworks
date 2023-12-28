import numgames as ng
dasquare = ng.Object()

while True:
  if ng.keydown(ng.KEY_BACKSPACE):
    break

  ng.draw_rect(dasquare.posx,dasquare.posy,dasquare.posx+dasquare.width,dasquare.posy+dasquare.height,"black")

  if ng.keydown(ng.KEY_TOOLBOX):
    del dasquare
