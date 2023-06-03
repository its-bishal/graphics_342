
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from typing import Tuple
import numpy as np

x_max = 400
y_max = 400
x_min = -400
y_min = -400

coordinate = Tuple[float, float, float]
ColorRGB = Tuple[float, float, float]
def draw_line(point1: coordinate, point2: coordinate, color: ColorRGB = (1.0, 1.0, 1.0)):
    glBegin(GL_LINE_STRIP)
    glColor3fv(color)
    glVertex3dv(point1)
    glVertex3dv(point2)
    glEnd()

def translate(point: coordinate, x_translation:int, y_translation:int, z_translation:int):
    x,y,z = point
    m = ([x],[y],[z],[1])
    tx_m = ([1,0,0,x_translation], [0,1,0,y_translation], [0,0,1,z_translation],[0,0,0,1])
    xT, yT, zT, _ = np.dot(tx_m, m)
    return xT[0], yT[0], zT[0]

def scale(point:coordinate, x_scale:int, y_scale:int, z_scale:int):
    x,y,z = point
    m = ([x], [y], [z], [1])
    scale_mat = ([x_scale, 0, 0, 0], [0, y_scale, 0, 0], [0, 0, z_scale, 0], [0,0,0,1])
    xT, yT, zT, _ = np.dot(scale_mat, m)
    return xT[0], yT[0], zT[0]

def rotation(point:coordinate, rotate: int):
    x,y,z = point
    m = ([x], [y], [z], [1])
    ang = np.deg2rad(rotate)
    translate_matrix = ([1, 0, 0, 0],
                        [0, np.cos(ang), -np.sin(ang), 0],
                        [0, np.sin(ang), np.cos(ang), 0],
                        [0, 0, 0, 1])
    
    xT, yT, zT, _ = np.dot(translate_matrix, m)
    return xT[0], yT[0], zT[0]


def main():
    pg.init()
    pg.display.set_mode((400,400), DOUBLEBUF|OPENGL|GL_RGB)
    pg.display.set_caption("3D transformations")

    gluPerspective(120, 1, 0, 200)
    glTranslatef(-10, -10, -100)

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()
        
        p1 = (3, 17, 37)
        p2 = (17, 29, 31)

        # colors
        yellow  = (1, 1, 0)
        teal    = (0, 1, 1)
        white   = (1, 1, 1)
        _w   = (0.5, 1, 0.5)

        draw_line((0, 0, 0), (200, 0, 0), (1, 0, 0)) # x-axis
        draw_line((0, 0, 0), (0, 200, 0), (0, 1, 0)) # y-axis
        draw_line((0, 0, 0), (0, 0, 200), (0, 0, 1)) # z-axis
        draw_line(p1, p2, yellow) # original

        trans_p1 = translate(p1, 10, 20, 30)
        trans_p2 = translate(p2, 10, 20, 30)
        draw_line(trans_p1, trans_p2, teal) # translated

        rot_p1 = rotation(p1, 30)
        rot_p2 = rotation(p2, 30)
        draw_line(rot_p1, rot_p2, white) # rotated

        sca_p1 = scale(p1, 3, 5, 2)
        sca_p2 = scale(p2, 3, 5, 2)
        draw_line(sca_p1, sca_p2, _w) # scaled

        pg.display.flip()

main()