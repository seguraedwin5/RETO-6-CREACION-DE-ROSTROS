
#crear cabello
def crearCabello(imagen):
    pelo = []
    for simbolo in range(0,7):
        pelo.append(imagen)
    return pelo

#crear ojos 1 un caracter
def crearOjos1(imgOjo):
    ojos = []
    for simboloojo in range(0,7):
        if simboloojo == 2 or simboloojo == 4:
            ojos.insert(simboloojo, imgOjo)
        else:
            ojos.insert(simboloojo,'  ')
    return ojos

#crear ojos sospechosos
def crearOjos2(imgOjo):
    ojos = []
    for simboloojo in range(0,7):
        if  simboloojo == 3:
            ojos.insert(simboloojo, imgOjo)
        else:
            ojos.insert(simboloojo,'  ')
    return ojos

#crear nariz y orejas
def crearNariz(imgNariz):
    nariz = []
    for simbolonariz in range(0,7):
       if  simbolonariz == 0:
            nariz.insert(simbolonariz, imgNariz)
       else:
          nariz.insert(simbolonariz,'  ')
    return nariz

#crear boca
def crearboca(imgBoca):
    boca = []
    for simboloboca in range(0,7):
        if  simboloboca == 3:
            boca.insert(simboloboca, imgBoca)
        else:
            boca.insert(simboloboca,'  ')
    return boca

#crear mentón
def crearmenton(imgMenton):
    menton = []
    for simbolomenton in range(0,7):
        if  simbolomenton == 1:
            menton.insert(simbolomenton, imgMenton)
        else:
            menton.insert(simbolomenton,'  ')
    return menton

