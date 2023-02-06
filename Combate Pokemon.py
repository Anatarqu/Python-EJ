from random import randint
import os

VIDA_INICIAL_PIKACHU= 80
VIDA_INICIAL_SQUIRTLE= 90
TAMANIO_BARRA_VIDA= 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
  #Se inician los turnos de combate

  print ("Combate Pokemon")
  barra_vida_pikachu = int (vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
  print("Pikachu:   [{} {}] ({}/{})" .format ("*" * barra_vida_pikachu," " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU)) 

  barra_vida_squirtle = int (vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
  print("Squirtle:  [{} {}] ({}/{})" .format ("*" * barra_vida_squirtle," " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE)) 
  
  input ("Enter para continuar... \n\n")
  os.system ("cls")
  
  # Turno de Pikachu
  print ("Turno de Pikachu")
  ataque_pikachu = randint (1,2)
  if ataque_pikachu == 1:
    #Bola Voltio
    print ("Pikachu ataca con Bola Voltio")
    vida_squirtle -= 10

  else:
    #Onda Trueno
    print("Pikachu ataca con Onda Trueno")
    vida_squirtle -= 11 

  
  if vida_squirtle < 0:
     vida_squirtle = 0

  if vida_pikachu < 0:
     vida_pikachu = 0
    

  barra_vida_pikachu = int (vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
  print("Pikachu:   [{} {}] ({}/{})" .format ("*" * barra_vida_pikachu," " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU)) 

  barra_vida_squirtle = int (vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
  print("Squirtle:  [{} {}] ({}/{})" .format ("*" * barra_vida_squirtle," " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE)) 

  print ("La vida de Pikachu es: {} y la vida de Squirtle es: {}" .format   
  (vida_pikachu, vida_squirtle))  

  input ("Enter para continuar... \n\n")
  os.system ("cls")

  #Turno de Squirtle
  print ("Turno de Squirtle")
  ataque_squirtle =None
  
  while ataque_squirtle not in ["P","A","B","N"]:
    ataque_squirtle = input ("Que ataque deseas realizar?  [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

  if ataque_squirtle == "P":
    #Placaje
    print ("Squirtle ataca con Placaje")
    vida_pikachu -= 10
  elif ataque_squirtle == "A":
    #Pistola Agua
    print ("Squirtle ataca con Pistola de Agua")
    vida_pikachu -= 12
  elif ataque_squirtle =="B":
    #Burbuja
    print ("Squirtle ataca con Burbuja")
    vida_pikachu -= 9
  elif ataque_squirtle =="N":
    #Nada
    print ("Squirtle no hace nada...")

  print ("La vida de Pikachu es: {} y la vida de Squirtle es: {}" .format   
  (vida_pikachu, vida_squirtle))  

  if vida_squirtle < 0:
     vida_squirtle = 0

  if vida_pikachu < 0:
     vida_pikachu = 0

  barra_vida_pikachu = int (vida_pikachu * TAMANIO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
  print("Pikachu:   [{} {}] ({}/{})" .format ("*" * barra_vida_pikachu," " * (TAMANIO_BARRA_VIDA - barra_vida_pikachu),vida_pikachu,VIDA_INICIAL_PIKACHU)) 

  barra_vida_squirtle = int (vida_squirtle * TAMANIO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
  print("Squirtle:  [{} {}] ({}/{})" .format ("*" * barra_vida_squirtle," " * (TAMANIO_BARRA_VIDA - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE)) 

  input("Enter para continuar... \n\n")
  os.system("cls")

if vida_pikachu > vida_squirtle:
  print ("Pikachu gana!")
else:
  print ("Squirtle gana!")
  