import random
import readchar
import os

# para saber que tipo de juego
game_tipe = None
while game_tipe != "1" and game_tipe != "2" and game_tipe != "3":
    game_tipe = input("¿Que tipo de juego deseas jugar? \n"
                      "Facil[1], Normal[2], Dificil[3]\n")



vidas = [80, 90, 95]
vid_temp = 1
vid_temp1 = 1
grafic_vida = 0
grafic_vida1 = 0
pika = vidas[1]
vida_personajes = []  
numero_personajes = 0
if game_tipe == "1":
    numero_personajes = 1
elif game_tipe == "2":
    numero_personajes = 2
else:
    numero_personajes = 3


while numero_personajes > len(vida_personajes):
    vida_personajes.append(vidas[random.randint(0, 2)])
  
# pokemon
pokemon = ["Pikachu", "Charmander", "Bulbasor", "Squirtle", "Blastoise", "Charizard", "Venasaur"]
ataques = [5, 8, 10, 16]
temp_atac = 0
string_atac = ""

# map
my_position = [1, 1]  
pos_x = 0
pos_y = 1
barrera = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x            xxxxxxx           xx
xxxxxx x xx x x x x  x      x  xx
x  xxxxxxxxxxxxxxxx             x
xxxxx x  xxxxx xxxxxxxx      xxxx
xxxxxxxxxxxxxxxxx              xx
xxxx xxxxx xxxxxx xxxxx xxxx xxxx
x  xxxxxxxxxxxxxxxxxx           x
xxx xx xxxx x  x x   x x x   x  x 
x                         xx    x
xx x x xx xxx x xxxxxxxx x x xx x
x                               x
x x x xxx x xx x  x xx x x x x xx 
x                               x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
"""
barrera = [list(row) for row in barrera.split("\n")]
map_width = len(barrera[0])  
map_height = len(barrera)  

maestros = []
while (len(maestros)) < numero_personajes:
    new_pos = ([random.randint(0, (map_width - 1)), random.randint(0, (map_height - 1))])

    if new_pos not in maestros and new_pos != my_position and \
            barrera[new_pos[pos_y]][new_pos[pos_x]] != "x":
        maestros.append(new_pos)
num_poke = 0  

while True:  
    os.system("cls")
    print("[W(arriba) S(abajo) A(izquierda) D(derecha)] \n"
          "X[para salir]")
    print(maestros)  
    print("+" + "-" * (map_width * 3) + "+")  
    for coordinate_y in range(map_height): 
        print("|", end="")  
        for coordinate_x in range(map_width): 
            char_to_draw = " "  
            objet_in_cell = None  
            for map_objet in maestros:  
                if map_objet[pos_x] == coordinate_x and map_objet[pos_y] == coordinate_y:  
                    char_to_draw = "◙"  
                    objet_in_cell = map_objet  

            if my_position[pos_x] == coordinate_x and \
                    my_position[pos_y] == coordinate_y:  
                char_to_draw = "◀"  
                if objet_in_cell:  
                    vid_temp = pika
                    vid_temp1 = vida_personajes[num_poke] 
                    input("Entrando al campo de batalla... \n "
                          "[presiona enter para continuar]")
                    while True:
                        os.system("cls")  
                        grafic_vida = int((vid_temp / pika) * 20)
                        grafic_vida1 = int((vid_temp1 / vida_personajes[num_poke]) * 20)
                     
                        print(pokemon[0] + " vs " + pokemon[num_poke + 1])
                        print("Vida " + pokemon[0] + " ({})".format(vid_temp))
                        print("♡" * grafic_vida)
                        print("Vida " + pokemon[num_poke + 1] + " ({})".format(vid_temp1))
                        print("♡" * grafic_vida1)
                        if game_tipe == "1":
                            temp_atac = ataques[random.randint(0, 1)]
                        elif game_tipe == "2":
                            temp_atac = ataques[random.randint(0, 2)]
                        else:
                            temp_atac = ataques[random.randint(2, 3)]
                        vid_temp -= temp_atac
                        if temp_atac == ataques[0]:
                            string_atac = "puñetazo"
                        elif temp_atac == ataques[1]:
                            string_atac = "patada"
                        elif temp_atac == ataques[2]:
                            string_atac = "pistola"
                        else:
                            string_atac = "bombaaa"
                        print(pokemon[num_poke + 1] + " ataco con " + string_atac)
                        temp_atac = 0
                        while string_atac not in ["4", "3", "2", "1", "F", "f"]:
                            string_atac = input("Elige un ataque:\n"
                                                "[1] [2] [3] [4] \n"
                                                "[F] (pasar turno)")
                        if string_atac == "1":
                            temp_atac = ataques[0]
                        elif string_atac == "2":
                            temp_atac = ataques[1]
                        elif string_atac == "3":
                            temp_atac = ataques[2]
                        elif string_atac == "4":
                            temp_atac = ataques[3]
                        else:
                            pass
                        vid_temp1 -= temp_atac
                        if temp_atac == ataques[0]:
                            string_atac = "puñetazo"
                        elif temp_atac == ataques[1]:
                            string_atac = "patada"
                        elif temp_atac == ataques[2]:
                            string_atac = "pistola"
                        elif temp_atac == 0:
                            string_atac = ", ¡nada! Pasaste turno."
                        else:
                            string_atac = "bombaaa"
                        print(pokemon[0] + " ataco con " + string_atac)
                        input("Presiona enter para continuar")
                     
                        if vid_temp <= 0 or vid_temp1 <= 0:
                            break
                    if vid_temp1 <= 0 and num_poke == (numero_personajes - 1):
                        os.system("cls")
                        input("¡Felicidades! siempre supe que lo lograrias. \n"
                              "¡Eres el/la mejor! \n"
                              "Presiona enter para salir mi ¡Crack!")
                        break
                    elif vid_temp1 <= 0:

                        input("¡Felicidades sigue asi! ¡Ya falta poco! \n"
                              "[Presiona enter para continuar]")
                        os.system("cls")
                        vid_temp1 = 6
                        vid_temp = 6

                    elif vid_temp <= 0:
                        os.system("cls")
                        input("¡Rayos! Hemos Perdido \n"
                              "Espero la proxima tengas mas suerte..."
                              "[Presiona enter para continuar]")
                        break

                    maestros.remove(objet_in_cell)

                    num_poke += 1

            # obstaculos
            if barrera[coordinate_y][coordinate_x] == "x":
                char_to_draw = "☱"
            print(" {} ".format(char_to_draw), end="")  
        print("|")
    print("+" + "-" * (map_width * 3) + "+")  
    """por si alguien esta leyendo mi codigo tuve problemas para salir del
    while por eso repeti esta linea de codigo otra vez"""
    if vid_temp1 <= 0 and num_poke == (numero_personajes - 1):
        os.system("cls")
        break

    elif vid_temp <= 0:
        os.system("cls")
        break

    direction = readchar.readchar()  

    new_pos = None

    # movimiento
    if direction in ["W", "w"]:
        new_pos = [my_position[pos_x], (my_position[pos_y] - 1)]
    elif direction in ["s", "S"]:
        new_pos = [my_position[pos_x], (my_position[pos_y] + 1)]
    elif direction in ["a", "A"]:
        new_pos = [(my_position[pos_x] - 1), (my_position[pos_y])]
    elif direction in ["D", "d"]:
        new_pos = [(my_position[pos_x] + 1), (my_position[pos_y])]
    elif direction in ["X", "x"]:
        break
    else:
        pass
    if new_pos:
        if barrera[new_pos[pos_y]][new_pos[pos_x]] != "x":
            my_position = new_pos