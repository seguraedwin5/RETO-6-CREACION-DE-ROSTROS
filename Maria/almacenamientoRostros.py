
def listarRostros():
    archivo = open("./Almacenamiento/Rostros.txt","r\n")
    for linea in archivo:
        print(linea)
    archivo.close()

def EscribirRostro(lista):
    archivo = open("./Almacenamiento/Rostros2.txt","a")
    for linea in range(0,len(lista)):
        if linea == 0:
            archivo.write(str(lista[linea]) + ":\n")
        else:
            archivo.write(str(lista[linea]) + "\n")
    archivo.write("\n")
    print("Archivo guardado Correctamente")
    archivo.close()
