
import pygame as pg
from pygame import display, event
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


coordinate = tuple[int, int]

def mid_point_ellipse(center: coordinate = (0,0), x_radius:int=1, y_radius:int=1):
    x_center, y_center = center

    x=0
    y=y_radius

    coordinates:list[coordinate]=[]

    # decision parameters for region 1
    d1 = ((y_radius**2)-(x_radius*x_radius*y_radius)+(0.25*x_radius*x_radius))
    dx = 2*y_radius*y_radius*x
    dy = 2*x_center*x_radius*y


    while(dx<dy):
        coordinates.append((x+x_center, y+y_center))

        if d1<0:
            x+=1
            dx = dx + 2*(y_radius**2)
            d1 = d1 + dx + (y_radius**2)

        else:
            x+=1
            y-=1
            dx = dx + 2*(y_radius**2)
            dy = dy - 2*(x_radius**2)
            d1 = d1 + dx - dy + (y_radius**2)

    # decision parameters for region 2
    d2 = (((y_radius**2)*((x+0.5)**2)) + ((x_radius**2)*((y-1)**2))-(x_radius**2)*(y_radius**2))

    while y>=0:
        coordinates.append((x+x_center, y+y_center))

        if d2>0:
            y-=1
            x+=1
            dx = dx + 2*(y_radius**2)
            d2 = d2 + (x_radius**2)-dy

        else:
            y-=1
            x+=1
            dx = dx + 2*(y_radius**2)
            dy = dy - 2*(x_radius)
            d2 = d2 + dx - dy + (x_radius**2)

    return coordinates


def drawEllipse():
    x_center, y_center = (60,60)
    region = mid_point_ellipse((x_center, y_center), 20,30)

    xy_quarter: list[coordinate] = [(x[0]-x_center, x[1]-y_center)for x in region]
    negxy_quarter: list[coordinate] = [(-x[0]+x_center, x[1]-y_center)for x in region]
    xnegy_quarter: list[coordinate] = [(x[0]-x_center, -x[1]+y_center)for x in region]
    negxnegy_quarter: list[coordinate] = [(-x[0]+x_center, -x[1]+y_center)for x in region]


    for region in [xy_quarter, negxy_quarter, xnegy_quarter, negxnegy_quarter]:
        glBegin(GL_LINE_STRIP)
        glColor3f(0.0,0.0,1.0)
        for ver in region:
            x,y=ver
            glVertex2f(x,y)
        glEnd()


def main():
    pg.init()
    display.set_mode((700,700), DOUBLEBUF|OPENGL|GL_RGB)
    display.set_caption("mid-point ellipse drawing algorithm implementaion")

    gluPerspective(200,1,1,10)
    glTranslatef(0.0,0.0,-10)

    while True:
        for eve in event.get():
            if eve.type == pg.QUIT:
                pg.quit()
                quit()

        drawEllipse()
        display.flip()

main()