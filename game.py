import pygame as pg
from OpenGL.GL import *


class App:

    def __init__(self):
        pg.init()
        pg.display.set_mode((640,640), pg.OPENGL|pg.DOUBLEBUF)

        # initialize opengl
        glClearColor(0.1,0.2,0.3,1)
        self.mainloop()

    def mainloop(self):
        running=True
        while(running):
            for event in pg.event.get():
                if(event.type==pg.quit):
                    running = False
                
            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

        self.quit()

    def quit(self):
        pg.quit()


if __name__ == "__main__":
    myapp = App()