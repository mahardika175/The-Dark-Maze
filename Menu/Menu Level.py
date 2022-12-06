from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def blok():
    glColor3f(0.2,0.1,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-355, 325)
    glVertex2f(355, 325)
    glVertex2f(355, 165)
    glVertex2f(-355, 165)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-160, 40)
    glVertex2f(160, 40)
    glVertex2f(160, -40)
    glVertex2f(-160, -40)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-160, -90)
    glVertex2f(160, -90)
    glVertex2f(160, -170)
    glVertex2f(-160, -170)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-160, -220)
    glVertex2f(160, -220)
    glVertex2f(160, -300)
    glVertex2f(-160, -300)
    glEnd()



# Cek :
def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-600, 600, -600, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    blok()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600,600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
