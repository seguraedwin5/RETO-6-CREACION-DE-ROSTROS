listamercado= ["arroz","azucar","aceite","jugo"]
def listarRostros():
    archivo = open("./Almacenamiento/Rostros.txt","r")
    for linea in archivo:
        print(linea)
    archivo.close()

def EscribirRostro(lista):
    archivo = open("./Almacenamiento/Rostros.txt","w")
    for linea in range(0,len(lista)):
        archivo.write(lista[linea] + "\n")
    archivo.close()


listarRostros()
EscribirRostro(listamercado)
listarRostros()
