"""Python library for Numworks python GUIs"""
from ion import *
from lined import *
import time
keyDelay = 0.2

#Defining UI Widgets
class Box:
    elements = list()
    keyPressTime = 0

    def __init__(self):
        self.boxBasis = Element(self, posy=0, height=0)
        self.elements.append(self.boxBasis)
        self.selectedIndex = 0
        self.run = True

    def renderBackground(self):
      print("backg")
      pass

    def renderElements(self):
        for element in self.elements:
            element.render()

    def selectIndex(self, index):
        self.elements[self.selectedIndex].select(False)
        self.selectedIndex = index
        self.elements[self.selectedIndex].select(True)

    def stop(self):
        self.run = False

    def mainLoop(self):
        self.run = True
        self.elements.pop(0)
        self.selectIndex(self.selectedIndex)
        self.renderBackground()
        self.renderElements()
        while self.run:
            if keydown(KEY_TOOLBOX):
                self.run = False
            if keydown(KEY_OK) and time.monotonic()-self.keyPressTime>keyDelay*3:
                self.elements[self.selectedIndex].doCommand()
                self.renderElements()

            if keydown(KEY_UP) and time.monotonic()-self.keyPressTime>keyDelay:
                self.keyPressTime = time.monotonic()
                self.selectIndex(self.selectedIndex-1 if self.selectedIndex>0 else len(self.elements)-1)
                self.renderElements()

            if keydown(KEY_DOWN) and time.monotonic()-self.keyPressTime>keyDelay:
                self.keyPressTime = time.monotonic()
                self.selectIndex(self.selectedIndex+1 if self.selectedIndex+1<len(self.elements) else 0)
                self.renderElements()

            time.sleep(0.03)

        self.elements.insert(0, self.boxBasis)

class Element:
    def __init__(self,box:Box, posx=None, posy=None, height=None, width=None):
        self.box = box
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width
        self.selectable = False

    def pack(self):
        self.posx = 160-round(self.width/2)
        self.posy = self.box.elements[-1].posy+self.box.elements[-1].height+1
        self.box.elements.append(self)

class Selectable:
    def __init__(self, command=None):
        self.command = command

    def doCommand(self):
        if callable(self.command):
            self.command()
            self.box.renderBackground()
            self.box.renderElements()

class Button(Element, Selectable):
    def __init__(self, box:Box, text:str="",
                 command=None, param:list=(),
                 color=(120,120,120), boundaryColor=(192,192,192),
                 selectedColor=(208,208,208), selectedBoundaryColor=(192,192,192),
                 fontColor=(255,255,255), selectedFontColor=(0,0,0)):
        Element.__init__(self, box)
        Selectable.__init__(self, command)
        self.text = text
        self.textWidth = len(text)*12
        self.height = 18+4*2+2*2
        self.width = self.textWidth+2*2+1*2
        self.color = color
        self.boundaryColor = boundaryColor
        self.selectedColor = selectedColor
        self.fontColor = fontColor
        self.selectedFontColor = selectedFontColor
        self.selectedBoundaryColor = selectedBoundaryColor
        self.renderColor = color
        self.renderBoundaryColor = boundaryColor
        self.renderFontColor = fontColor
        self.selectable = True

    def select(self, selectBool:bool):
        if selectBool:
            self.renderColor = self.selectedColor
            self.renderBoundaryColor = self.selectedBoundaryColor
            self.renderFontColor = self.selectedFontColor
        else:
            self.renderColor = self.color
            self.renderBoundaryColor = self.boundaryColor
            self.renderFontColor = self.fontColor

    def render(self):
        draw_box(self.posx,self.posy,self.textWidth+4*2+2*2,18+4*2+2*2,self.renderBoundaryColor)
        draw_rect(self.posx+2, self.posy+2, self.textWidth+4*2, 18+4*2, self.renderColor)
        draw_string(self.text, self.posx+4+2, self.posy+4+2, self.renderFontColor, self.renderColor)
