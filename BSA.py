

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class BSA:
    def __init__(self):
        pg.init()
        pg.display.set_mode((700,700), pg.OPENGL|pg.DOUBLEBUF)
        pg.display.set_caption("Bresenhem line drawing algorithm")


    def dda(self,x1, x2, y1, y2):
        x,y = x1,y1

        dx = abs(x2-x1)
        dy = abs(y2-y1)

        steps = max(dx, dy)

        Xinc = dx/steps
        Yinc = dy/steps

        vertices=list[tuple[float, float]]

        for i in range(steps):
            vertices.append(x,y)
            x = x + Xinc
            y = y + Yinc
        return vertices
    
    def draw_DDA(self):
        
            coordinates = self.bsa((-1,-1), (2,2))

            glBegin(GL_LINES)
            glColor3f(0.4,0.6,0.9)

            for v in coordinates:
                x,y = v
                glVertex2f(x, y)
            glEnd()
                       

    def display(self):

        gluPerspective(200, 1, 1, 10)
        glTranslatef(0.0, 0.0, -10)

        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    quit()

            self.draw_DDA()
            pg.display.flip()


if __name__ == "__main__":
    BSA()