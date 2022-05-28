from collections import namedtuple
import pprint
import Maria.listasRostros as lr
import Maria.almacenamientoRostros as ar
import Maria.codificarRostros as codif


#Creacion de tupla Rostro
TupRostro = namedtuple('TupRostro',['Nombre','Cabello','Ojos','Nariz','Boca','Menton'])
RostroCompleto = []
#cabello
while True:
  try:
    opcioncabello = int(input("Elija el cabello que desea:\n 1 Crespo    ➰ \n 2 Rubio     🟨 \n 3 Café      🟫 \n 4 Negro     ⬛ \n 5 Peinado   〰 \n")) 
    if opcioncabello == 1:
      cabellocreado = lr.crearCabello('➰')
      print(''.join(cabellocreado))
      RostroCompleto.append(cabellocreado)
      break
    elif opcioncabello == 2:
      cabellocreado = lr.crearCabello('🟨')
      print(''.join(cabellocreado))
      RostroCompleto.append(cabellocreado)
      break
    elif opcioncabello == 3:
      cabellocreado = lr.crearCabello('🟫')
      print(''.join(cabellocreado))
      RostroCompleto.append(cabellocreado)
      break
    elif opcioncabello == 4:
      cabellocreado = lr.crearCabello('⬛')
      print(''.join(cabellocreado))
      RostroCompleto.append(cabellocreado)
      break
    elif opcioncabello == 5:
      cabellocreado = lr.crearCabello('〰')
      print(''.join(cabellocreado))
      RostroCompleto.append(cabellocreado)
      break
    else:
      opcioncabello 
      print("\n🚫Elija una opción correcto\n")
  except ValueError:
    print("\nIngrese un dígito de 1 a 5\n")
    continue

#ojos
while True:
  try:
    opcionojos = int(input("\nElija los ojos que desea:\n 1 Ojos pequeños  👁  👁 \n 2 Ojos OnFire    🔥 🔥 \n 3 Sospechosos     👀 \n 4 Corazón        💗 💗 \n 5 Orientales     ➖ ➖ \n"))
    if opcionojos == 1:
      ojoscreados = lr.crearOjos1('👁 ')
      print(''.join(ojoscreados))
      RostroCompleto.append(ojoscreados)
      break
    elif opcionojos == 2:
      ojoscreados = lr.crearOjos1('🔥')
      print(''.join(ojoscreados))
      RostroCompleto.append(ojoscreados)
      break
    elif opcionojos == 3:
      ojoscreados =lr.crearOjos2('👀')
      print(''.join(ojoscreados))
      RostroCompleto.append(ojoscreados)
      break
    elif opcionojos == 4:
      ojoscreados = lr.crearOjos1('💗')
      print(''.join(ojoscreados))
      RostroCompleto.append(ojoscreados)
      break
    elif opcionojos == 5:
      ojoscreados = lr.crearOjos1('➖')
      print(''.join(ojoscreados))
      RostroCompleto.append(ojoscreados)
      break
    else:
      print("\n🚫Elija una opción correcto\n")
  except ValueError:
    print("\nIngrese un dígito de 1 a 5\n")
    continue
print('\n -------Rostro Generado------- \n')
for fila in RostroCompleto:
  print(''.join(map(str, fila)))

#nariz/orejas
while True:
  try:
    opcionnariz = int(input("\nElija las orejas y nariz que desea:\n 1 Naríz normal     👂  👃  👂 \n 2 Nariz pequeña    👂   ω  👂 \n 3 Chanchito        👂  🐽  👂\n 4 Osito            👂  ㅅ  👂 \n 5 Lengua de señas  🦻  👃  🦻\n"))
    if opcionnariz == 1:
      narizcreada = lr.crearNariz('👂    👃    👂')
      print(''.join(narizcreada))
      RostroCompleto.append(narizcreada)
      break
    elif opcionnariz == 2:
      narizcreada =lr.crearNariz('👂     ω    👂')
      print(''.join(narizcreada))
      RostroCompleto.append(narizcreada)
      break
    elif opcionnariz == 3:
      narizcreada = lr.crearNariz('👂    🐽    👂')
      print(''.join(narizcreada))
      RostroCompleto.append(narizcreada)
      break
    elif opcionnariz == 4:
      narizcreada = lr.crearNariz('👂    ㅅ    👂')
      print(''.join(narizcreada))
      RostroCompleto.append(narizcreada)
      break
    elif opcionnariz == 5:
      narizcreada = lr.crearNariz('🦻    👃    🦻')
      print(''.join(narizcreada))
      RostroCompleto.append(narizcreada)
      break
    else:
      print("\n🚫Elija una opción correcto\n")
  except ValueError:
    print("\nIngrese un dígito de 1 a 5\n")
    continue
print('\n -------Rostro Generado------- \n')
for fila in RostroCompleto:
  print (''.join(map(str, fila)))

#boca
while True:
  try:
    opcionboca = int(input("\nElija la boca que desea:\n 1 Labios        👄 \n 2 Sacar lengua  👅 \n 3 Beso          ❌ \n 4 Grosería      💢 \n 5 Sin boca \n"))
    if opcionboca == 1:
      bocacreada = lr.crearboca('👄')
      print(''.join(bocacreada))
      RostroCompleto.append(bocacreada)
      break
    elif opcionboca == 2:
      bocacreada = lr.crearboca('👅')
      print(''.join(bocacreada))
      RostroCompleto.append(bocacreada)
      break
    elif opcionboca== 3:
      bocacreada = lr.crearboca('❌')
      print(''.join(bocacreada))
      RostroCompleto.append(bocacreada)
      break
    elif opcionboca == 4:
      bocacreada = lr.crearboca('💢')
      print(''.join(bocacreada))
      RostroCompleto.append(bocacreada)    
      break
    elif opcionboca == 5:
      bocacreada = lr.crearboca (' ')
      print(''.join(bocacreada)) 
      RostroCompleto.append(bocacreada)
      break
    else:
      print("\n🚫Elija una opción correcto\n")
  except ValueError:
    print("\nIngrese un dígito de 1 a 5\n")
    continue
print('\n -------Rostro Generado------- \n')
for fila in RostroCompleto:
  print (''.join(map(str, fila)))
    
#menton
while True:
  try:
    opcionmenton = int(input("\nElija el mentón que desea:\n 1 Plano       \_____/ \n 2 Barbilla    \__ˆ__/ \n 3 Sonriente   \__︶__/ \n 4 Barbilludo   \__±__/ \n 5 Coqueto     \__¸__/ \n"))
    if opcionmenton == 1:
      mentoncreado = lr.crearmenton('\_______/')
      print(''.join(mentoncreado))
      RostroCompleto.append(mentoncreado)
      break
    elif opcionmenton == 2:
      mentoncreado = lr.crearmenton('\___ˆ___/')
      print(''.join(mentoncreado))
      RostroCompleto.append(mentoncreado)
      break
    elif opcionmenton == 3:
      mentoncreado = lr.crearmenton('\___︶___/')
      print(''.join(mentoncreado))
      RostroCompleto.append(mentoncreado)
      break
    elif opcionmenton == 4:
      mentoncreado = lr.crearmenton('\___±___/')
      print(''.join(mentoncreado))
      RostroCompleto.append(mentoncreado)
      break
    elif opcionmenton == 5:
      mentoncreado = lr.crearmenton('\___¸___/')
      print(''.join(mentoncreado))
      RostroCompleto.append(mentoncreado)
      break
    else:
      print("\n🚫Elija una opción correcto\n")
  except ValueError:
    print("\nIngrese un dígito de 1 a 5\n")
  continue 
print('\n -------Rostro Generado------- \n')
for fila in RostroCompleto:
  print (''.join(map(str, fila)))

#Solicitar nombre del rostro
nombre = str(input("Digite el nombre para el rostro antes de guardar:"))
Rostrodecodificado = TupRostro(nombre,RostroCompleto[0],RostroCompleto[1],RostroCompleto[2],RostroCompleto[3],RostroCompleto[4])
_diccionarioRostro = Rostrodecodificado._asdict()
RostroCodificado = codif.codificar(_diccionarioRostro)

ar.EscribirRostrojson(RostroCodificado._asdict())
ar.ListarRostrosjson(ar.ObtenerRostrosjson())

