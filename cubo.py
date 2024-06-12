# Introdução à Computação Visual
# Trabalho 1
# renderização de um cubo com faces coloridas 
# que pode sofrer transformações de rotação, 
# translação e escalonamento.

# Rafael Renó Corrêa, 2022000403
# 12 de junho de 2024

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1),
    (1, 1, -1)
)

arestas = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 7),
    (1, 6),
    (2, 5),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4)
)

def Cubo():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0, 0, -10)

    # desenha a cubo
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # limpa o buffer
    
    Cubo()

    pygame.display.flip() # atualiza a tela
    #

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

main()