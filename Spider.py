from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def badan():
    # glScale(2.0, 2.0, 0.0)
    glColor3f(1.0,0.0,0.0)
    #Badan
    glBegin(GL_POLYGON)
    glVertex2f(-1.142, 1.37)
    glVertex2f(-1.6, 1.37)
    glVertex2f(-1.6, -1.372)
    glVertex2f(1.6, -1.372)
    glVertex2f(1.6, 1.372)
    glVertex2f(1.142, 1.372)
    glVertex2f(1.142, 1.83)
    glVertex2f(-1.142, 1.83)
    glEnd()

    #Mata
    glColor3f(0.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.14, -0.456)#K
    glVertex2f(-0.684, -0.456)#L
    glVertex2f(-0.684, -0.916)#M
    glVertex2f(-1.14, -0.916)#n
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(1.14, -0.456)#K'
    glVertex2f(0.684, -0.456)#L'
    glVertex2f(0.684, -0.916)#M'
    glVertex2f(1.14, -0.916)#N'
    glEnd()



Pk = 0.456  #panjang segmen kaki
p = 0.912  #jarak antar kaki

def Kaki():
    # glScale(2.0, 2.0, 0.0)
    glColor3f(1.0,0.0,0.0)
    #Kaki Kiri
    #pangkal depan
    glBegin(GL_POLYGON)
    glVertex2f(-1.6, -0.46-p)#0
    glVertex2f(-2.512+Pk, -0.46-p)#P
    glVertex2f(-2.512+Pk, -0.92-p)#Q
    glVertex2f(-1.6, -0.92-p)#R
    glEnd()



    #pangkal tengah1
    glBegin(GL_POLYGON)
    glVertex2f(-1.6, -0.46)
    glVertex2f(-2.512, -0.46)
    glVertex2f(-2.512, -0.92)
    glVertex2f(-1.6, -0.92)
    glEnd()

    #pangkal tengah2
    glBegin(GL_POLYGON)
    glVertex2f(-1.6, -0.46+p)
    glVertex2f(-2.512, -0.46+p)
    glVertex2f(-2.512, -0.92+p)
    glVertex2f(-1.6, -0.92+p)
    glEnd()

    #pangkal belakang
    glBegin(GL_POLYGON)
    glVertex2f(-1.6, -0.46+2*p)
    glVertex2f(-2.512, -0.46+2*p)
    glVertex2f(-2.512, -0.92+2*p)
    glVertex2f(-1.6, -0.92+2*p)
    glEnd()

    #Kaki Kanan
    #pangkal depan
    glBegin(GL_POLYGON)
    glVertex2f(1.6, -0.46-p)
    glVertex2f(2.512, -0.46-p)
    glVertex2f(2.512, -0.92-p)
    glVertex2f(1.6, -0.92-p)
    glEnd()
    #pangkal tengah1
    glBegin(GL_POLYGON)
    glVertex2f(1.6, -0.46)
    glVertex2f(2.512, -0.46)
    glVertex2f(2.512, -0.92)
    glVertex2f(1.6, -0.92)
    glEnd()

    #pangkal tengah2
    glBegin(GL_POLYGON)
    glVertex2f(1.6, -0.46+p)
    glVertex2f(2.512, -0.46+p)
    glVertex2f(2.512, -0.92+p)
    glVertex2f(1.6, -0.92+p)
    glEnd()

    #pangkal belakang
    glBegin(GL_POLYGON)
    glVertex2f(1.6, -0.46+2*p)
    glVertex2f(2.512, -0.46+2*p)
    glVertex2f(2.512, -0.92+2*p)
    glVertex2f(1.6, -0.92+2*p)
    glEnd()


# Cek :
# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-4, 4, -3, 4, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     badan()
#     Kaki()
#     glutSwapBuffers()
    
# print("",((2.512-1.6)/2))
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()
