
def listarRostros():
    archivo = open("./Almacenamiento/Rostros.txt","r\n")
    for linea in archivo:
        print(linea)
    archivo.close()

def EscribirRostro(lista):
    archivo = open("./Almacenamiento/Rostros2.txt","a")
    for linea in range(0,len(lista)):
        archivo.write(str(lista[linea]) + "\n")
    archivo.close()
