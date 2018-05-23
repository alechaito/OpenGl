from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

spin  = 0

def main():
    #iniciando
    glutInit()
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize (800, 800)
    glutInitWindowPosition(300, 300)
    glutCreateWindow ("Teapots World")
    glEnable(GL_DEPTH_TEST)

    ##ILUMINACAO
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    position = [0.0, 0.0, 0.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    mdiffuse = [1.0, 0.0, 1.0, 1.0]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mdiffuse)
    ################
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


def display():
    global spin
    ##inicializando
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    spin = spin + 0.1
    if (spin > 360.0):
        spin = spin - 360.0
    #################### CRIANDO primeiro teapot
    glPushMatrix()
    glRotatef(spin, 0.0, 0.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidTeapot(0.15)
    glPopMatrix()
    ###################### CRIANDO segundo teapot
    glLoadIdentity()
    glPushMatrix()
    glRotatef(spin, 0.0, 0.0, 1.0)
    glTranslatef(0.5, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glutSolidTeapot(0.15)
    glPopMatrix()
    ##################### CRIANDO terceiro teapot
    glLoadIdentity()
    glPushMatrix()
    glTranslatef(-0.5,0.0,0.0)
    glRotatef(spin, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 0.0)
    glutSolidTeapot(0.15)
    glPopMatrix()
    glLoadIdentity()
    glutSwapBuffers()
    glutPostRedisplay()


def reshape():
   w = 800
   h = 800
   glViewport (0, 0, w, h)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(-w, w, -h, h, -50000.0, 50000.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt(0.0,-1.0,0.0, 0.0,15000.0, 0.0, 0.0,0.0,1.0)

def drawn_cube():
    glLoadIdentity()
    glPushMatrix()
    glRotatef(spin, 0.0, 0.0, 1.0)
    glTranslatef(0.5, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glEnd()
    glPopMatrix()

main()