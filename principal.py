#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Rapido...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        #fonde 
        imagen_redimensionada=pygame.transform.scale(COLOR_FONDO, (900, 600))

        puntos = 0
        candidata = ""
        silabasEnPantalla = []
        posiciones = []
        listaDeSilabas=[]
        lemario=[]

        archivo= open("silabas.txt","r", encoding="latin-1")
        listaDeSilabas = lectura(archivo, listaDeSilabas)

        archivo2= open("lemario.txt","r", encoding="latin-1")
        lemario = lectura(archivo2, lemario)

        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()
            if True:
            	fps = 3

            #Muestra el game over
            if segundos >= 0 and segundos <= 0.50:
                silabasEnPantalla = []
                posiciones = []
                posiciones.append(Punto(320,250))
                silabasEnPantalla.append("GAME OVER")
            
            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata, silabasEnPantalla, posiciones, lemario)
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
            #Limpiar pantalla anterior
            screen.blit(imagen_redimensionada,[-60,0])

            #Dibujar de nuevo todo
            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos)

            pygame.display.flip()

            actualizar(silabasEnPantalla, posiciones, listaDeSilabas)

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
