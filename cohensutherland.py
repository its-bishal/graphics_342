
#cohensutherland line clipping 
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from typing import Tuple

# Region codes
Inside = 0  #0000
Left = 1    #0001
Right = 2   #0010
Buttom = 4  #0100
Top = 8     #1000

x_max = 400
y_max = 400
x_min = -400
y_min = -400

coordinate = Tuple[float, float]

def define_code(point: coordinate):
    x, y = point
    code = Inside
    if x < x_min:
        code |= Left
    elif x > x_max:
        code |= Right
    if y < y_min:
        code |= Buttom
    elif y > y_max:
        code |= Top
    return code

def draw_line(point1: coordinate, point2: coordinate):
    x1, y1 = point1
    x2, y2 = point2
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def CohenSutherlandClip(point1: coordinate, point2: coordinate):
    x1, y1 = point1
    x2, y2 = point2
    code1 = define_code(point1)
    code2 = define_code(point2)

    accept = False

    while True:
        #endpoints lie within rectangle
        if code1 == Inside and code2 == Inside:
            accept = True
            break
        #endpoints lie outside rectangle
        elif (code1 & code2) != Inside:
            break
        #endpoints lie on rectangle boundary
        #find intersection point
        else:
            x = 1.0
            y = 1.0
            if code1 == Left:
                x = x_min
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            elif code1 == Right:
                x = x_max
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code1 == Buttom:
                y = y_min
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            elif code1 == Top:
                y = y_max
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            
            #update endpoints
            if code1 != 0:
                x1 = x
                y1 = y
                code1 = define_code((x1, y1))
            if code2 != 0:
                x2 = x
                y2 = y
                code2 = define_code((x2, y2))
        
    if accept:
        draw_line((x1, y1), (x2, y2))

      
def main():
    pg.init()
    pg.display.set_mode((500,500), DOUBLEBUF|OPENGL|GL_RGB)
    pg.display.set_caption('cohen-sutherland line clipping algorithm')

    glTranslatef(0.0,0.0,0.0)
    gluOrtho2D(-500, 500, -500, 500)

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()
        

        # draw clipping lines
        draw_line((x_min,y_min), (x_max,y_min))
        draw_line((x_max,y_min), (x_max,y_max))
        draw_line((x_min,y_min), (x_min,y_max))
        draw_line((x_min,y_max), (x_max,y_max))

        CohenSutherlandClip((650, -215), (100, 190))
        CohenSutherlandClip((-750, 115), (110, 160))
        
        pg.display.flip()

main()
