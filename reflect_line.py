import numpy as np
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

coordinate = [float, float]

def reflection_on_Y(point : coordinate):
    x, y = point
    m = ([x], [y], [1])
    reflect_mat = ([-1, 0, 0], [0, 1, 0], [0, 0, 1])
    xT, yT, _ = np.dot(reflect_mat, m)
    return xT[0], yT[0]

def reflection_on_X(point : coordinate):
    x, y = point
    m = ([x], [y], [1])
    reflect_mat = ([1, 0, 0], [0, -1, 0], [0, 0, 1])
    xT, yT, _ = np.dot(reflect_mat, m)
    return xT[0], yT[0]

def draw():
    start_pt : coordinate = (-1,-2)
    end_pt : coordinate = (3,4)

    stX_tps = reflection_on_X(start_pt)
    endX_tps = reflection_on_X(end_pt)
    stY_tps = reflection_on_Y(start_pt)
    endY_tps = reflection_on_Y(end_pt)

    glBegin(GL_LINES)
    glColor3f(0.4,0.6,0.7)
    glVertex2f(start_pt[0], start_pt[1])
    glVertex2f(end_pt[0], end_pt[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.1,0.2,0.9)
    glVertex2f(stX_tps[0], stX_tps[1])
    glVertex2f(endX_tps[0], endX_tps[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.4,0.9,0.9)
    glVertex2f(stY_tps[0], stY_tps[1])
    glVertex2f(endY_tps[0], endY_tps[1])
    glEnd()



def main():
    pg.init()
    pg.display.set_mode((600,600), DOUBLEBUF | OPENGL | GL_RGB)
    pg.display.set_caption("reflection in line")

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