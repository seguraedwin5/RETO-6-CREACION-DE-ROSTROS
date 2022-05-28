from collections import namedtuple

def codificar(diccionarioRostro:dict):
    Rostrocod = namedtuple('Rostrocod',['Nombre','Cabello','Ojos','Nariz','Boca','Menton'])
    #Listas de las  caracteristicas sin codificar
    _Nombre = diccionarioRostro.get("Nombre")
    _Cabello = diccionarioRostro.get("Cabello")
    _Ojos = diccionarioRostro.get("Ojos")
    _Nariz = diccionarioRostro.get("Nariz")
    _Boca = diccionarioRostro.get("Boca")
    _Menton = diccionarioRostro.get("Menton")
    
    Nombrecod =contarelementos(_Nombre)
    Cabellocod = contarelementos(_Cabello)
    Ojoscod =contarelementos(_Ojos)
    Narizcod = contarelementos(_Nariz)
    Bocacod = contarelementos(_Boca)
    Mentoncod = contarelementos(_Menton)
    #listas codificadas
    return Rostrocod(_Nombre,Cabellocod,Ojoscod,Narizcod,Bocacod,Mentoncod)

    
    #print(f"\n{_Nombre}\n{_Cabello}\n{_Ojos}\n{_Nariz}\n{_Boca}\n{_Menton}")

def decodificar(rostroArchivo):
    pass

def contarelementos(ListaCaracteristica:list):
    listacodigo=[]
    itemactual = ''
    contador = 0
    for numitem in range(0,len(ListaCaracteristica)+1):
        if numitem == 0:
            itemactual = ListaCaracteristica[numitem]
        elif numitem == len(ListaCaracteristica):
            itemactual = ListaCaracteristica[numitem-1]
            contador += 1
            listacodigo.extend([contador,itemactual])
        else:
            itemanterior = itemactual
            itemactual = ListaCaracteristica[numitem]
            if itemactual == itemanterior:
                contador += 1
            else:
                contador += 1
                listacodigo.extend([contador,itemanterior])
                contador = 0
    return listacodigo


        
        


    
        

        
            
    
    