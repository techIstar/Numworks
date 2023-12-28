"""
    ====================
    Raycasting engine
    for NumWorks

    author: Kevin FEDYNA
    ====================
"""

# Dependencies
from kandinsky import fill_rect
from ion import keydown
from math import radians, cos, sin
import time

# Player objects (vectors)
player = [4.5, 5.5]
player_dir = [-1, 0]
plane = [0, 0.66]
rotation = 0.1

# Map object (tuple) 
world = (255, 149, 133, 245, 133, 165, 129, 255)
bits = 8

# Global variables
w = 320
h = 222
res = 80

def vision():
    fill_rect(0, 0, w, h, (0,)*3)
    for x in range(res):

        visible_x = 2 * x / res - 1
        player_int = [int(c) for c in player]
        side_dist = [0, 0]
        step = [0, 0]
        ray = tuple(player_dir[i] + plane[i] * visible_x for i in range(2))
        d_dist = tuple(ray[i] != 0 and abs(1 / ray[i]) or 0 for i in range(2))

        if ray[0] < 0:
            step[0] = -1
            side_dist[0] = (player[0] - player_int[0]) * d_dist[0]
        else:
            step[0] = 1
            side_dist[0] = (1 + player_int[0] - player[0]) * d_dist[0]
        if ray[1] < 0:
            step[1] = -1
            side_dist[1] = (player[1] - player_int[1]) * d_dist[1]
        else:
            step[1] = 1
            side_dist[1] = (1 + int(player[1]) - player_int[1]) * d_dist[1]

        while "in air":
            if side_dist[0] < side_dist[1]:
                side_dist[0] += d_dist[0]
                player_int[0] += step[0]
                side = 0
            else:
                side_dist[1] += d_dist[1]
                player_int[1] += step[1]
                side = 1
            if world[player_int[1]] >> (bits - 1 - player_int[0]) & 1:
                break

        temp = ray[side] != 0 and ((player_int[side] - player[side] + (1 - step[side]) / 2) / ray[side]) or 0
        wall_h = temp != 0 and h / temp or 0
        draw_top = int(-wall_h / 2 + h / 2)
        draw_top = draw_top > 0 and draw_top or 0
        draw_bottom = int(wall_h / 2 + h / 2)
        draw_bottom = draw_bottom >= h and h or draw_bottom

        fill_rect(x * w//res, draw_top, w // res, draw_bottom - draw_top, side and (255, )*3 or (200,)*3)

# Core
def main():
    global player_dir, plane, player
    vision()
    while not (keydown(4) or keydown(17)):
        loop_start_time = time.monotonic()
        changed = False
        if keydown(3):
            player_dir = [player_dir[0] * cos(-rotation) - player_dir[1] * sin(-rotation),
                        player_dir[0] * sin(-rotation) + player_dir[1] * cos(-rotation)]
            plane = [plane[0] * cos(-rotation) - plane[1] * sin(-rotation),
                    plane[0] * sin(-rotation) + plane[1] * cos(-rotation)]
            changed = True
        if keydown(0):
            player_dir = [player_dir[0] * cos(rotation) - player_dir[1] * sin(rotation),
                        player_dir[0] * sin(rotation) + player_dir[1] * cos(rotation)]
            plane = [plane[0] * cos(rotation) - plane[1] * sin(rotation),
                    plane[0] * sin(rotation) + plane[1] * cos(rotation)]
            changed = True
        if keydown(1) and not world[int(player[1] + player_dir[1] / 20)] >> (bits - 1 - int(player[0] + player_dir[0] / 20)) & 1:
            player[0] += player_dir[0] / 20
            player[1] += player_dir[1] / 20
            changed = True
        if keydown(2) and not world[int(player[1] - player_dir[1] / 20)] >> (bits - 1 - int(player[0] - player_dir[0] / 20)) & 1:
            player[0] -= player_dir[0] / 20
            player[1] -= player_dir[1] / 20
            changed = True

        if changed:
            vision()

        if time.monotonic() - loop_start_time < 0.03:
            timeToWait = 0.03 - (time.monotonic() - loop_start_time)
            time.sleep(timeToWait)

#tweaking
player = [4.66266681802921, 5.170213236960046]
player_dir = [-0.36235775447667423, -0.9320390859672281]
plane = [-0.6151457967383703, 0.23915611795460484]
res = 320
