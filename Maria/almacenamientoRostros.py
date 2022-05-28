import json
from operator import indexOf
import pprint
import Maria.codificarRostros as codif

def listarRostros():
    rostrolista = []
    archivo = open("./Almacenamiento/Rostros2.txt","r")
    for linea in archivo:
        rostrolista.append(linea)
    archivo.close()
    return rostrolista

# def EscribirRostro(lista):
#     archivo = open("./Almacenamiento/Rostros2.txt","a")
#     for linea in range(0,len(lista)):
#         if linea == 0:
#             archivo.write(str(lista[linea]) + ":\n")
#         else:
#             archivo.write(str(lista[linea]) + "\n")
#     archivo.write(";\n")
#     print("Archivo guardado Correctamente")
#     archivo.close()



def EscribirRostrojson(dictRostro:dict):
    listadict = []
    with open("./Almacenamiento/Rostros.json","r") as archivo:#open
        listadict = json.load(archivo)


    with open("./Almacenamiento/Rostros.json","w") as archivo:
        listadict.append(dictRostro)#transformar
        json.dump(listadict, archivo, indent=4)#guardar y Cerrar

#se Recibe la lista de diccionarios de rostros y los imprime 
def ListarRostrosjson(Listadrostros):
    for elemento in Listadrostros:
        rostrodec = codif.decodificar(elemento)
        codif.mostrarRostrodecodif(rostrodec)
        print("\n")
            
        
def ObtenerRostrosjson():
    listadatos = [] #crear lista vacia
    with open("./Almacenamiento/Rostros.json","r") as archivo: #Abrir Archivo json
        listadatos = json.load(archivo) #transformar lo que esta en el archivo json en lista de diccionarios
    return listadatos #retorna la lista de diccionarios

def ObtenerRostroporNombre(NombreRostro:str):
    listadicrostros = []
    with open("./Almacenamiento/Rostros.json","r") as archivo:
        listadicrostros = json.load(archivo)
    for dicc in listadicrostros:
        if dicc["Nombre"] == NombreRostro:
            resultado = dicc#retorna el diccionario
    if resultado == None:
        return "No se encontró el resultado"
    return resultado



    
