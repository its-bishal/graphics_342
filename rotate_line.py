
import numpy as np
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

coordinate = [float, float]

def rotation(point:coordinate, rotate: int):
    x,y = point
    m = ([x], [y], [1])
    ang = np.deg2rad(rotate)
    translate_matrix = ([np.cos(ang), -np.sin(ang), 0],
                        [np.sin(ang), np.cos(ang), 0],
                        [0, 0, 1])
    
    xT, yT, _ = np.dot(translate_matrix, m)
    return xT[0], yT[0]

def draw():
    start_pt : coordinate = (1,1)
    end_pt : coordinate = (6,7)

    rot_angle = 150

    start_tpt = rotation(start_pt, rot_angle)
    end_tpt = rotation(end_pt, rot_angle)

    glBegin(GL_LINES)
    glColor3f(0.7, 0.2, 0.3)
    glVertex2f(start_pt[0], start_pt[1])
    glVertex2f(end_pt[0], end_pt[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.4, 0.6, 0.1)
    glVertex2f(start_tpt[0], start_tpt[1])
    glVertex2f(end_tpt[0], end_tpt[1])
    glEnd()

def main():
    pg.init()
    pg.display.set_mode((600,600), DOUBLEBUF | OPENGL | GL_RGB)
    pg.display.set_caption("rotation in line")

    gluPerspective(60, 1, 1, 10)
    glTranslatef(0.0,0.0,-10)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()

        draw()
        pg.display.flip()

main()