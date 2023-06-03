

import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


coordinate = tuple[int, int]
# mid-point circle drawing algorithm
def mid_point_circle(center : coordinate() =(0,0), radius : int = 1):
    
    x_center, y_center = center

    coordinates: list[coordinate] = []

    # moving anti-clockwise from the x-axis
    x = radius
    y = 0

    # axes after translation
    coordinates.append((x+x_center,y+y_center))

    if radius>0:
        coordinates.append((x + x_center, -y + y_center))
        coordinates.append((y + x_center, x + y_center))
        coordinates.append((-y + x_center, x + y_center))

    p = 1 - radius
    while x>y:
       y+=1

    #    midpoint inside or on the perimeter
       if p<=0:
           p = p + 2*y + 1
    #    midpoint outside the perimeter
       else:
           x-=1
           p = p + 2*y - 2*x +1
    
       
       coordinates.append((x+x_center,y+y_center))
       coordinates.append((-x+x_center,y+y_center))
       coordinates.append((x+x_center,-y+y_center))
       coordinates.append((-x+x_center,-y+y_center))


       if x!=y:
           
           coordinates.append((y+x_center, x+y_center))
           coordinates.append((-y+x_center, x+y_center))
           coordinates.append((y+x_center, -x+y_center))
           coordinates.append((-y+x_center, -x+y_center))

    return coordinates


def draw_circle():
    x_center, y_center = (0,0)
    region = mid_point_circle((x_center, y_center), 25)

    xy_quarter: list[coordinate] = [(x[0]-x_center, x[1]-y_center)for x in region]
    negxy_quarter: list[coordinate] = [(-x[0]+x_center, x[1]-y_center)for x in region]
    xnegy_quarter: list[coordinate] = [(x[0]-x_center, -x[1]+y_center)for x in region]
    negxnegy_quarter: list[coordinate] = [(-x[0]+x_center, -x[1]+y_center)for x in region]

    for reg in [xy_quarter, negxy_quarter, xnegy_quarter, negxnegy_quarter]:
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0,0.0,1.0)
        for vertex in reg:
            x,y = vertex
            glVertex2f(x,y)

        glEnd()


def main():
    pg.init()
    display.set_mode((700,700), DOUBLEBUF|OPENGL|GL_RGB)
    display.set_caption('CIrcle using mid-point algorithm')

    gluPerspective(200,1,1,10)
    glTranslatef(0.0,0.0,-10)

    while True:
        for ev in event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()

        draw_circle()
        display.flip()

main()
