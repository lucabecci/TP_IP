
def lectura(archivo, lista):
    lista = archivo.readlines()
    nueva_lista = []
    for i in range(len(lista)):
        nueva_lista.append(lista[i].strip())
    lista = nueva_lista

archivo= open("silabas.txt","r", encoding="latin-1")
silabas = []


silabas = lectura(archivo, silabas)

print(silabas)
