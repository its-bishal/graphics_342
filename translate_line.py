

import numpy as np
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

coordinate = tuple[float, float]

def translate(point: coordinate, x_translation:int, y_translation:int):
    x,y = point
    m = ([x],[y],[1])
    tx_m = ([1,0,x_translation], [0,1,y_translation],[0,0,1])
    xT, yT, _ = np.dot(tx_m, m)
    return xT[0], yT[0]



def draw():
    start_pt : coordinate = (-1,-2)
    end_pt : coordinate = (3,4)
    translation_pt = (1,2)

    start_tpt = translate(start_pt, translation_pt[0], translation_pt[1])
    end_tpt = translate(end_pt, translation_pt[0], translation_pt[1])

    glBegin(GL_LINES)
    glColor3f(0.4,0.6,0.7)
    glVertex2f(start_pt[0], start_pt[1])
    glVertex2f(end_pt[0], end_pt[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.1,0.2,0.9)
    glVertex2f(start_tpt[0], start_tpt[1])
    glVertex2f(end_tpt[0], end_tpt[1])
    glEnd()

def main():
    pg.init()
    pg.display.set_mode((600,600), DOUBLEBUF | OPENGL | GL_RGB)
    pg.display.set_caption('line- translation')

    gluPerspective(55, 1, 1, 10)
    glTranslatef(0.0,0.0,-10)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()
        draw()
        pg.display.flip()


main()        
            