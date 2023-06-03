
import pygame as pg

from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from typing import Tuple


def BSA(start: Tuple[int,int],end: Tuple[int,int]):
    x1, y1 = start
    x2, y2 = end

    m  = abs((y2 - y1)/(x2 - x1))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    vertices : list[Tuple[int,int]] = []
    
    if m < 1:
        for i in range(0, dx):
            p = 2 * dy - dx
            x = x + 1
            if p < 0:
                vertices.append((x, y))
                p = p + 2 * dy
            else:
                y = y + 1
                vertices.append((x, y))
                p = p + 2 * (dy - dx)
    else:
        for i in range(0, dy):
            p = 2 *dx - dy
            y = y + 1
            if p < 0:
                vertices.append((x, y))
                p = p + 2 * dx
            else:
                x = x + 1
                vertices.append((x, y))
                p = p + 2 * (dx - dy)
    return vertices


def plot_BSA():

    vertices = BSA((-1,-1), (2,2))

    glBegin(GL_LINES)
    glColor3f(0.4,0.6,0.9)

    for v in vertices:
        x,y = v
        glVertex2f(x, y)
    glEnd()


def main():
    pg.init()
    display.set_mode((600, 600), DOUBLEBUF|OPENGL|GL_RGB)
    display.set_caption("Bresenhem line drawing algorithm")

    gluPerspective(90, 1, 1, 6)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        plot_BSA()
        display.flip()

main()