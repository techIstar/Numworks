#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pynput import keyboard as kb
from sys import exit

KEY_LEFT = kb.Key.left
KEY_UP = kb.Key.up
KEY_DOWN = kb.Key.down
KEY_RIGHT = kb.Key.right
KEY_OK = kb.Key.enter
KEY_BACK = None
KEY_HOME = None
KEY_ONOFF = None
KEY_SHIFT = None
KEY_ALPHA = None
KEY_XNT = None
KEY_VAR = None
KEY_TOOLBOX = kb.Key.shift_r
KEY_BACKSPACE = kb.Key.backspace
KEY_EXP = None
KEY_LN = None
KEY_LOG = None
KEY_IMAGINARY = None
KEY_COMMA = None
KEY_POWER = None
KEY_SINE = None
KEY_COSINE = None
KEY_TANGENT = None
KEY_PI = None
KEY_SQRT = None
KEY_SQUARE = None
KEY_SEVEN = None
KEY_EIGHT = None
KEY_NINE = None
KEY_LEFTPARENTHESIS = None
KEY_RIGHTPARENTHESIS = None
KEY_FOUR = None
KEY_FIVE = None
KEY_SIX = None
KEY_MULTIPLICATION = None
KEY_DIVISION = None
KEY_ONE = None
KEY_TWO = None
KEY_THREE = None
KEY_PLUS = None
KEY_MINUS = None
KEY_ZERO = None
KEY_DOT = None
KEY_EE = None
KEY_ANS = None
KEY_EXE = None

keypad_dict = {0: KEY_LEFT,
               1: KEY_UP,
               2: KEY_DOWN,
               3: KEY_RIGHT,
               4: KEY_OK,
               5: KEY_BACK,
               6: KEY_HOME,
               8: KEY_ONOFF,
               12: KEY_SHIFT,
               13: KEY_ALPHA,
               14: KEY_XNT,
               15: KEY_VAR,
               16: KEY_TOOLBOX,
               17: KEY_BACKSPACE,
               18: KEY_EXP,
               19: KEY_LN,
               20: KEY_LOG,
               21: KEY_IMAGINARY,
               22: KEY_COMMA,
               23: KEY_POWER,
               24: KEY_SINE,
               25: KEY_COSINE,
               26: KEY_TANGENT,
               27: KEY_PI,
               28: KEY_SQRT,
               29: KEY_SQUARE,
               30: KEY_SEVEN,
               31: KEY_EIGHT,
               32: KEY_NINE,
               33: KEY_LEFTPARENTHESIS,
               34: KEY_RIGHTPARENTHESIS,
               36: KEY_FOUR,
               37: KEY_FIVE,
               38: KEY_SIX,
               39: KEY_MULTIPLICATION,
               40: KEY_DIVISION,
               42: KEY_ONE,
               43: KEY_TWO,
               44: KEY_THREE,
               45: KEY_PLUS,
               46: KEY_MINUS,
               48: KEY_ZERO,
               49: KEY_DOT,
               50: KEY_EE,
               51: KEY_ANS,
               52: KEY_EXE}


pressed_keys = list()

def keydown(k):
    if isinstance(k,int):
        k = keypad_dict[k]
    if k in pressed_keys:
        return True
    else:
        return False

def on_press(key):
    global pressed_keys
    if not key in pressed_keys:
        pressed_keys.append(key)

def on_release(key):
    global pressed_keys
    if key in pressed_keys:
        pressed_keys.remove(key)

# Collect events until released
#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#listener.join()

# ...or, in a non-blocking fashion:
listener = kb.Listener(on_press=on_press, on_release=on_release)
listener.start()
