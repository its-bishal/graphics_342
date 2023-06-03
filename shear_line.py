import numpy as np
import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

coordinate = [float, float]

def shear(point: coordinate, x_shear:int, y_shear: int):
    x, y = point
    m = ([x], [y], [1])
    xm_shear = ()

    xm_shear = ([1, x_shear, 0], [0, 1, 0], [0, 0, 1])
    ym_shear = ([1, 0, 0], [y_shear, 1, 0], [0, 0, 1])
    
    composite_m = np.dot(xm_shear, ym_shear)
    sheared_m = np.dot(composite_m, m)
    
    xT, yT, _ = sheared_m
    return (xT[0], yT[0])


def draw():
    st_point: Coordinate = (-4,-6)
    end_point: Coordinate = (7,3)
    shear_By = (2,1)

    st_tps = shear(st_point, shear_By[0], shear_By[1])
    end_tps = shear(end_point, shear_By[0], shear_By[1])
    
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(st_point[0], st_point[1])
    glVertex2f(end_point[0], end_point[1])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(st_tps[0], st_tps[1])
    glVertex2f(end_tps[0], end_tps[1])
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