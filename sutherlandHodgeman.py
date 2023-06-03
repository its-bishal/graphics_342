
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

# POINTS NEED TO BE PRESENTED CLOCKWISE OR ELSE THIS WONT WORK
def is_inside(p1,p2,q):
    R = (p2[0] - p1[0]) * (q[1] - p1[1]) - (p2[1] - p1[1]) * (q[0] - p1[0])
    if R <= 0:
        return True
    else:
        return False

def compute_intersection(p1,p2,p3,p4):
    
    # if first line is vertical
    if p2[0] - p1[0] == 0:
        x = p1[0]

        m2 = (p4[1] - p3[1]) / (p4[0] - p3[0])
        b2 = p3[1] - m2 * p3[0]

        y = m2 * x + b2
    
    # if second line is vertical
    elif p4[0] - p3[0] == 0:
        x = p3[0]
        
        m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b1 = p1[1] - m1 * p1[0]

        y = m1 * x + b1
    
    # if neither line is vertical
    else:
        m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b1 = p1[1] - m1 * p1[0]
        
        m2 = (p4[1] - p3[1]) / (p4[0] - p3[0])
        b2 = p3[1] - m2 * p3[0]

        x = (b2 - b1) / (m1 - m2)

        y = m1 * x + b1
    
    intersection = (x,y)
    
    return intersection

def clip(subject_polygon,clipping_polygon):
    
    final_polygon = subject_polygon.copy()
    
    for i in range(len(clipping_polygon)):
        
        # stores the vertices of the next iteration of the clipping procedure
        next_polygon = final_polygon.copy()
        
        # stores the vertices of the final clipped polygon
        final_polygon = []
        
        # these two vertices define a line segment (edge) in the clipping polygon
        c_edge_start = clipping_polygon[i - 1]
        c_edge_end = clipping_polygon[i]
        
        for j in range(len(next_polygon)):
            
            # these two vertices define a line segment (edge) in the subject
            s_edge_start = next_polygon[j - 1]
            s_edge_end = next_polygon[j]
            
            if is_inside(c_edge_start,c_edge_end,s_edge_end):
                if not is_inside(c_edge_start,c_edge_end,s_edge_start):
                    intersection = compute_intersection(s_edge_start,s_edge_end,c_edge_start,c_edge_end)
                    final_polygon.append(intersection)
                final_polygon.append(tuple(s_edge_end))
            elif is_inside(c_edge_start,c_edge_end,s_edge_start):
                intersection = compute_intersection(s_edge_start,s_edge_end,c_edge_start,c_edge_end)
                final_polygon.append(intersection)
    
    return np.asarray(final_polygon)


def draw_polygon(clipped_polygon):
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for i in range(len(clipped_polygon)):
        x,y = clipped_polygon[i]
        glVertex2f(x,y)
    glEnd()

def main():
    pg.init()
    pg.display.set_mode((500,500), DOUBLEBUF|OPENGL|GL_RGB)
    pg.display.set_caption('sutherland Hodgeman Polygon clipping algorithm')

    glTranslatef(0.0,0.0,0.0)
    gluOrtho2D(-500, 500, -500, 500)

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                quit()
       
        subject_polygon = [(0,30), (250,250), (-300,0), (0,-300), (-250,-250), (-300, 0), (-250,0)]
        clipping_polygon = [(-2,-2),(-2,2),(2,2),(2,-2)]
    

        subject_polygon = np.array(subject_polygon)
        clipping_polygon = np.array(clipping_polygon)
        clipped_polygon = clip(subject_polygon,clipping_polygon)

        draw_polygon(clipped_polygon)
            
        pg.display.flip()

main()