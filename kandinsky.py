#!/usr/bin/env python3
"""Imitates the beavior of the numworks kandisky module"""
# -*- coding: utf-8 -*-

#setting up the pixel amplifier, renders bigger pixels by a factor of 'amplifier'
WIDTH = 320
HEIGHT = 222
amplifier = 1
if amplifier > 0 and amplifier < 5 and isinstance(amplifier, int):
    WIDTH = 320 * amplifier
    HEIGHT = 222 * amplifier
else:
    amplifier = 1
    print('Uncorrect amplifier size set to default')

#importing needed modules
import pygame
from multiprocessing import Process
from sys import exit

#initialization of pygame
pygame.display.set_caption('Numworks')
icon = pygame.image.load('numworks_icon.png')
pygame.display.set_icon(icon)
pygame.display.init()
pygame.font.init()

font = pygame.font.SysFont("arial", 16)

#defining useful functions to simulate the numworks kandinsky module
def get_pixel(x,y):
    pass

def color(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)
    return pygame.Color(r, g, b)

def set_pixel(x: int, y: int, color):
    if isinstance(color, str):
        color = pygame.Color(color)
    pygame.draw.rect(screen, color, pygame.Rect(x * amplifier, y * amplifier, amplifier, amplifier))
    pygame.display.flip()

#TODO add a /n interpreter cause this thing is dumb
def draw_string(text: str, x: int, y: int, font_color=(0,0,0), backg_color=(255,255,255)):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, False, font_color, backg_color)
        scaled_surface = pygame.transform.scale(text_surface, (text_surface.get_width() * amplifier, text_surface.get_height() * amplifier))
        screen.blit(scaled_surface, (x * amplifier, y * amplifier + i * font.get_linesize()))
    pygame.display.flip()




def fill_rect(x: int, y: int, w: int, h: int, col):
    if isinstance(col, str):
        col = pygame.Color(col)
    pygame.draw.rect(screen, col, pygame.Rect(x * amplifier, y * amplifier, w * amplifier, h * amplifier))
    pygame.display.flip()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Numworks")
screen.fill((255, 255, 255))
pygame.display.flip()

pressed_keys = list()
def screen_loop():
    global pressed_keys
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.flip()
    pygame.display.quit()
    pygame.font.quit()
screen_thread = Process(target=screen_loop)
screen_thread.start()
