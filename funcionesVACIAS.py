from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math

def lectura(archivo, lista):
    lista = archivo.readlines()
    nueva_lista = []
    for i in range(len(lista)):
        nueva_lista.append(lista[i].strip())
    lista = nueva_lista
    return lista


def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    ## eliminar viejas y baja las palabras
    for i in range(len(silabasEnPantalla)-1,-1,-1):
        if(posiciones[i].y < ALTO-90):
            posiciones[i] = Punto(posiciones[i].x, (posiciones[i].y+5))
        else:
            silabasEnPantalla.pop(i)
            posiciones.pop(i)
    ##evita superposiciones
    ocupadosX=[]
    ## agregar nuevas
    if(len(posiciones)==0 or posiciones[len(posiciones)-1].y > 15 ):
        silaba=nuevaSilaba(listaDeSilabas)
        x=random.randrange(0,ANCHO-20)
        while(estaCerca(x,ocupadosX)):
            x=random.randrange(0,ANCHO-20)
        ocupadosX.append(x)
        posiciones.append(Punto(x,-1))
        silabasEnPantalla.append(silaba)

def estaCerca(elem, lista):
    for num in lista:
       if (abs(elem-num)<15):
           return True
    return False

def nuevaSilaba(silabas):
    return silabas[random.randint(0, len(silabas) - 1)]

def quitar(candidata, silabasEnPantalla, posiciones):
    for i in silabasEnPantalla:
        if candidata == silabasEnPantalla[i].strip():
            posiciones.pop(i)
            silabasEnPantalla.pop(i)
        
def dameSilabas(candidata):
    candidata = separador(candidata)
    listaSilabas = []
    silaba = ""
    print(candidata)
    for x in range(0, len(candidata)):
        if candidata[x] != "-":
            silaba += candidata[x]
        else:
            listaSilabas.append(silaba)
            silaba=""
        if len(listaSilabas) == x:
            listaSilabas.append(silaba)


def esValida(candidata, silabasEnPantalla, lemario):
    silaba = silabasEnPantalla[0]
    silabasLista = dameSilabas(candidata)
    for x in candidata:
        if x == silaba:
            return True
    return False

def Puntos(candidata):
        pass

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    dameSilabas(candidata)
    # esValida(candidata, silabasEnPantalla, lemario)
    pass
