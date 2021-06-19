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
    if len(silabas) != 0:
        return silabas[random.randint(0, len(silabas) - 1)]

def quitar(candidata, silabasEnPantalla, posiciones):
    silabasCandidata = dameSilabas(candidata)
    for x in silabasCandidata:
        borrarValor(x, silabasEnPantalla, posiciones)

def borrarValor(silaba, silabasEnPantalla, posiciones):
    for x in range(0, len(silabasEnPantalla)):
        if silabasEnPantalla[x] == silaba:
            silabasEnPantalla.pop(x)
            posiciones.pop(x)
            return 
       
def dameSilabas(candidata):
    candidata = separador(candidata)
    listaSilabas = []
    silaba = ""
    for x in range(0, len(candidata)):
        if candidata[x] != "-":
            silaba += candidata[x]
        else:
            listaSilabas.append(silaba)
            silaba=""
        if x == len(candidata) - 1:
            listaSilabas.append(silaba)
    return listaSilabas

def esValida(candidata, silabasEnPantalla, lemario):
    silabasLista = dameSilabas(candidata)
    encontradas = 0
    aEncontrar = len(silabasLista)
    for x in range(0, len(silabasLista)):
        if silabasLista[x] in silabasEnPantalla:
            encontradas += 1
    if aEncontrar == encontradas:
        for i in range(0, len(lemario)):
            if candidata == lemario[i]:
                return True
    return False

def esVocal(letra):
    vocal="aeiou"
    for x in vocal:
        if x == letra:
            return True
    return False

def esDificil(letra):
    dificil="jkqwxyz"
    for x in dificil:
        if x == letra:
            return True
    return False

def Puntos(candidata):
    puntos = 0
    for x in candidata:
        if esVocal(x):
            puntos += 1
        elif esDificil(x):
            puntos += 5
        elif not esVocal(x) and not esDificil(x):
            puntos += 2
    return puntos

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    puntaje = 0
    if candidata == "":
        return puntaje
    if esValida(candidata, silabasEnPantalla, lemario) == True:
        quitar(candidata,silabasEnPantalla,posiciones)
        puntaje = Puntos(candidata)
    return puntaje

#funciones de configuracion

