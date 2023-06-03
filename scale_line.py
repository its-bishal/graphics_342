import numpy as np
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

coordinate = [float, float]

def scale(point:coordinate, x_scale:int, y_scale:int):
    x,y = point
    m = ([x], [y], [1])
    scale_mat = ([x_scale, 0, 0], [0, y_scale, 0], [0,0,1])
    xT, yT, _ = np.dot(scale_mat, m)
    return xT[0], yT[0]

def draw():
    start_pt : coordinate = (-1,-2)
    end_pt : coordinate = (3,4)
    scale_pt = (1,2)

    start_tpt = scale(start_pt, scale_pt[0], scale_pt[1])
    end_tpt = scale(end_pt, scale_pt[0], scale_pt[1])

    glBegin(GL_LINES)
    glColor3f(0.4,0.6,0.7)
    glVertex2f(start_pt[0], start_pt[1])
    glVertex2f(end_pt[0], end_pt[1])
    # drawText('original line')
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.1,0.2,0.9)
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