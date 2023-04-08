import random

tupla= ("piedra", "papel", "tijera" )
ganador_computadora=0
ganador_persona=0
empate = 0
rondas = 1

while True: 

  print("-----" * 10)
  print("Ronda", rondas)
  print("-----" * 10)
  print("puntaje de la computadora:", ganador_computadora)
  print("puntaje de la persona:",ganador_persona)

  
  opciones= input("piedra, papel o tijera: ")
  opciones= opciones.lower()
  rondas += 1
  if not opciones in tupla:
    print("Esa opcion no es valida")
    continue
    
  computadora= random.choice(tupla)
  
  print("opcion de l usuario: " ,opciones)
  print("opcion de la computadora: " ,computadora)
  
  if opciones== computadora :
     print("Empate")
  elif opciones == "piedra":
    if computadora == "tijera": 
      print("La piedra gana a la tijera")
      print("    ")
      print("******EL USUARIO GANO******")
      print("    ")
      ganador_persona +=1
    else:
      print ("El papel gana a la Piedra")
      print("    ")
      print("******LA COMPUTADORA GANA******")
      print("    ")
      ganador_computadora +=1
  elif opciones == "papel":
    if computadora == "piedra":
      print("El papel gana a la piedra")
      print("    ")
      print("******EL USUARIO GANO******")
      print("    ")
      ganador_persona +=1
    else:
      print ("las tijeras gana al papel")
      print("    ")
      print("******LA COMPUTADORA GANA******")
      print("    ")
      ganador_computadora +=1
  elif opciones == "tijera":
    if computadora == "papel":
      print("las tijeras le gana al papel")
      print("    ")
      print("******EL USUARIO GANO******")
      print("    ")
      ganador_persona +=1
    else:
      print("La piedra le gana a la tijera")
      print("    ")
      print("******LA COMPUTADORA GANA******")
      print("    ")
      ganador_computadora +=1

  if ganador_computadora==2:
    print("*****" * 10)
    print("*****" * 10)
    print("*****" * 10)
    print("*******EL ROTUNDO GANADOR ES LA COMPUTADORA*******")
    print("*****" * 10)
    print("*****" * 10)
    print("*****" * 10)
    break
  if ganador_persona == 2:
    print("*****" * 10)
    print("*****" * 10)
    print("*****" * 10)
    print("*********EL ROTUNDO GANADOR ES LA PERSONA*********")
    print("*****" * 10)
    print("*****" * 10)
    print("*****" * 10)
    break