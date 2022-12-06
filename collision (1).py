from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Koordinat x dan y untuk posisi kotak
pos_x_kotak = 0
pos_y_kotak = 0

pos_x_apel = 0
pos_y_apel = 0

hijau = 1
biru = 1
merah = 1

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

# Membuat bentuk kotak
def apel():
    global pos_x_apel, pos_y_apel, pos_x_kotak, pos_y_kotak

    glPushMatrix()
    glColor3f(merah,0,0)
    glTranslated(pos_x_apel,pos_y_apel,0)

    glBegin(GL_TRIANGLES)
    # Kiri Atas
    glVertex2f(20,-50)
    # Kanan Atas
    glVertex2f(50,-50)
    # Kanan Bawah
    glVertex2f(50,50)
    # Kiri Bawa
    glEnd()
    glPopMatrix()

def kotak():
    global pos_x_kotak, pos_y_kotak
    glPushMatrix()
    glColor3f(hijau,biru,merah)
    if pos_x_kotak >= 445:
        pos_x_kotak = 445

    elif pos_x_kotak <= -445:
        pos_x_kotak = -445


    # glTranslated(pos_x_kotak, pos_y_kotak, 0)
    print("pos_x_kotak=",pos_x_kotak)
    glTranslated(pos_x_kotak,pos_y_kotak, 0)
    glTranslated(50,50,0)
    glBegin(GL_POLYGON)
    glVertex2f(-100,-100)
    glVertex2f(0,-100)
    glVertex2f(0,0)
    glVertex2f(-100,0)
    glEnd()
    glPopMatrix()

def collision():
    if (pos_x_apel-50<=pos_x_kotak+50<=pos_x_apel+50 or pos_x_apel-50<=pos_x_kotak-50<=pos_x_apel+50) and (pos_y_apel-50<=pos_y_kotak+50<=pos_y_apel+50 or pos_y_apel-50<=pos_y_kotak-50<=pos_y_apel+50):
        print('colli')
    elif (pos_x_apel-50<=pos_x_kotak+50<=pos_x_apel+50 or pos_x_apel-50<=pos_x_kotak-50<=pos_x_apel+50):
        print('Overlap sumbu x')
    elif (pos_y_apel-50<=pos_y_kotak+50<=pos_y_apel+50 or pos_y_apel-50<=pos_y_kotak-50<=pos_y_apel+50):
        print('Overlap sumbu y')
    else :
        print('None')

def colliMouse(x,y):
    x=-250+x
    y=250-y
    if pos_x_apel-50<= x<=pos_x_apel+50 and pos_y_apel-50<= y <=pos_y_apel+50 :
        print('Tertekan')
    else:
        print('Tidak kena')

    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.)
    glBegin(GL_LINES)
    glVertex2f(-500.0, 0.0)
    glVertex2f(500.0, 0.0)
    glVertex2f(0.0, 500.0)
    glVertex2f(0.0, -500.0)
    glEnd()
    kotak()
    apel()
    collision()
    glFlush()

def input_keyboard(key,x,y):
    global pos_x_kotak, pos_y_kotak
    if key == GLUT_KEY_UP:
        pos_y_kotak += 10
    elif key == GLUT_KEY_DOWN:
        pos_y_kotak -= 5
    elif key == GLUT_KEY_RIGHT:
        pos_x_kotak += 5
    elif key == GLUT_KEY_LEFT:
        pos_x_kotak -= 5
    collision()

def input_mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        colliMouse(x,y)
        

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("collision")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    # glutSpecialFunc(input_mouse)
    glutTimerFunc(1,update,0)
    init()
    glutMainLoop()

main()