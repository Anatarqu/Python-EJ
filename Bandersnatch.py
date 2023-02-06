import random

titulo = "Bandersnatch"
coger_llave = False
coger_tarjeta = False
coger_papel = False
numero1_papel = random.randint(1, 100)
numero2_papel = random.randint(1, 100)
codigo_papel = numero1_papel + numero2_papel
texto_error = "Respuesta Invalida"

print("\n" + titulo + "\n" + "--------------------------------" "\n")

print("Despiertas en tu casa pero no ves a nadie de tus familiares ni a tu mascotas\n"
     "Decides ponerte en pie, todo está silencioso y parece que estas solo.\n")

decision_celda = input("¿Que decides hacer?\n"
                       "A - Gritar en busca de ayuda.\n"
                       "B - Tratar de salir de tu pieza.\n"
                       "C - Investigar la habitación\n"
                       "D - Volver a dormirte.\n")

if decision_celda == "A":
    print("\nTe acercas a la puerta y llamas a tus padres en busca de ayuda, parece que alguien se acerca.\n"
          "Aparece una persona desconocida, no se ve sorprendido al verte.\n"
          "Dice que dejes de hacer ruido, y con una bara fina de metal te pega en             la cabeza \n"
          "Caes al suelo y debido a la lesión que tenías en tu cabeza mueres.\n"
          "- FIN DEL JUEGO -")
    exit()

elif decision_celda == "B":
    print("\nTe acercas a la puerta y buscas abrirla pero esta cerrada.\n"
          "Tratas de forzarla pero es inutíl, parece que alguien se acerca.\n"
          "Aparece una persona desconocida, no se ve sorprendido al verte.\n"
          "Dice que dejes de hacer ruido, y con una bara fina de metal te pega en             la cabeza \n"
          "Caes al suelo y debido a la lesión que tenías en tu cabeza mueres.\n"
          "- FIN DEL JUEGO -")
    exit()

elif decision_celda == "C":
    print("\nDecides investigar la habitación, pero no son tus cosas, no es tu cama, no es tu televisor y no ves tus fotos.\n"
          "Al mirar bajo la cama encuentras un cuerpo, tu cuerpo.\n"
          "Investigas el cuerpo y encuentras una llave.\n")

    decision_llave = input("¿Quieres coger la llave? (S/N) ")

    if decision_llave == "S":
        coger_llave = True

        print("Decides coger la llave y sigues buscando, y encuentras una tarjeta blanca con el texto Bandersnatch\n"
              "grabada en ella.\n")

        decision_tarjeta = input("¿Quieres coger la tarjeta? (S/N) ")

        if decision_tarjeta == "S":
            coger_tarjeta = True
            print("Coges la tarjeta\n")

        elif decision_tarjeta == "N":
            coger_tarjeta = False
            print("No coges la tarjeta\n")

        else:
            print(texto_error)
            exit()

        print("Tras mirar un poco más encuentras un papel, parece que no hay nada escrito\n")

        decision_papel = input("¿Quieres coger el papel? (S/N) ")

        if decision_papel == "S":
            coger_papel = True
            print("Coges el papel\n")

        elif decision_papel == "N":
            coger_papel = False
            print("No coges el papel\n")

        else:
            print(texto_error)
            exit()

        print("Te acercas a la puerta e intentas probar suerte, ¡BINGO!, logras abrir la puerta utilizando la llave\n"
        "pero te encuentras con cosas diferentes en tu casa, .\n"
        "es como si ya no fuera tuya y ves en el pasillo el camino .\n")

        decision_camino = input("¿Que camino escoges?\n"
                                "A - Derecha\n"
                                "B - Izquierda\n")

        if decision_camino == "A":
            print("\nDecides ir a la derecha y tras un par de minutos te encuentras con una trampilla, parece accesible.")

            decision_trampilla = input("¿Que decides hacer?\n"
                                       "A - Entrar por la trampilla\n"
                                       "B - Seguir tu camino\n")

            if decision_trampilla == "A":
                print("\nCrees que la mejor idea es entrar por la trampilla.\n"
                      "El camino es muy estrecho, pero encuentras la salida \n"
                      "Te encuentras en una habitación con 2 puertas, una sin cerradura y la otra con un lector de\n"
                      "tarjetas blancas.\n")

                decision_puerta = input("¿Que puerta escoges?\n"
                                        "A - La puerta sin cerradura\n"
                                        "B - La puerta del lector amarillo\n")

                if decision_puerta == "A":
                   print("\nDecides abrir la puerta sin cerradura y tras abrirla te encuentras de nuevo en tu habitación\n"
                         "como si no hubiera pasado nada\n"
                         "Has muerto.\n"
                         "- FIN DEL JUEGO -")
                   exit()

                elif decision_puerta == "B":
                    print("\nDecides acercarte a la puerta con el lector blanco y te das cuenta de que el lector\n")

                    if coger_tarjeta == True:
                        print("\nSacas la tarjeta blanca y la pasas por el lector.\n"
                              "La puerta se abre.\n"
                              "Por fin, la luz del...\n"
                              "Te das cuenta de que esto no es el mundo que conocias.\n"
                              "- FIN DEL JUEGO -\n")
                        exit()

                    else:
                        print("\nNo has cogido la tarjeta blanca por lo que decides forzar el lector.\n"
                              "Salta una alarma y escuchas que se abre la puerta sin cerradura.\n"
                              "tras abrirla te encuentras de nuevo en tu habitación\n"
                         "como si no hubiera pasado nada\n"
                         "Has muerto.\n"
                         "- FIN DEL JUEGO -")
                        exit()

                else:
                    print(texto_error)
                    exit()

            elif decision_trampilla == "B":
                print("\nSigues tu camino y en un par de minutos llegas a una puerta bloqueada con un código numérico.\n"
                      "Te acercas a ella, aparece una luz ultravioleta del techo y recuerdas el papel en\n"
                      "blanco que encontraste.\n")

                if coger_papel == True:
                    print("Sacas el papel y en el aparece una operación matemática, parece el número de salida.\n"
                          "Te acercas a la puerta y lees el papel para introducir el código.\n")

                    print("IMPORTANTE NO PERDER\n"
                          "CÓDIGO --> {} + {}".format(numero1_papel, numero2_papel))

                    codigo_introducido = input("- INTRODUZCA EL CODIGO -\n")

                    if codigo_introducido == codigo_papel:
                        print("\nEl código es correcto y la puerta se abre.\n"
                              "Al cruzarla te das cuenta de que ese no es el\n"
                              "mundo que conocias.\n"
                              "Avanzas unos metros y encuentras un portal con el nombre Bandersnatch.\n"
                              "El portal está apagado.\n"
                              "Lo examinas y encuentras un lector de tarjetas blanco.\n")

                        if coger_tarjeta == True:
                            print("Recuerdas que habias cogido una tarjeta Blanca de TU CUERPO \n"
                                  "encontraba en la habitación.\n"
                                  "Al pasar la tarjeta por el lector el portal se enciende.\n")

                            decision_portal = input("¿Cruzas el portal? (S/N) ")

                            if decision_portal == "S":
                                print("Decides cruzar el portal y...\n"
                                      "Despiertas de esa pesadilla, vuelves al mundo que conoces"
                                      "- FIN DEL JUEGO -")
                                exit()

                            elif decision_portal == "N":
                                print("Decides no cruzar el portal, parece peligroso.\n"
                                      "Pasas el resto de tus dias vagando por la casa \n "
                                      "sin salida.\n"
                                      "Atrapado, pero no muerto.\n"
                                      "- FIN DEL JUEGO -")
                                exit()

                            else:
                                print(texto_error)
                                exit()


                        else:
                            print("Te das cuenta de que no cogiste la tarjeta que se encontraba en\n"
                                  "tu cuerpo de tu pieza.\n"
                                  "Pasas el resto de tus dias vagando por la casa \n "
                                      "sin salida.\n"
                                      "Atrapado, pero no muerto.\n"
                                      "- FIN DEL JUEGO -")
                            exit()

                    else:
                        print("\nERROR - ERR0R - ERROR- ERROR\n"
                              "El código es incorrecto.\n"
                              "Comienza a sonar una alarma \n"
                              "Caes al suelo y se te nubla la vista.\n"
                              "Has muerto.\n"
                              "- FIN DEL JUEGO -")
                        exit()

                else:
                    print("\nRecuerdas que no cogiste el papel, golpeas la puerta a causa de la desesperación... \n"
                          "Caes al suelo y se te nubla la vista.\n"
                          "Has muerto.\n"
                          "- FIN DEL JUEGO -")
                    exit()

            else:
                print(texto_error)
                exit()

        elif decision_camino == "B":
            print("\nDecides ir a la izquierda.\n"
            "Llevas 1h andando y el pasillo no acaba, parece interminable.\n"
            "No hay salida.\n"
            "Te das la vuelta y sin fuerzas corres en la otra dirección.\n"
            "Corres, corres y corres en un pasillo sin fin... \n"
            "Has muerto\n"
            "- FIN DEL JUEGO -")
            exit()

        else:
            print(texto_error)
            exit()

    elif decision_llave == "N":
        print("\nCrees que la mejor decisión es no tocar TU cuerpo.\n"
              "No puedes volver a dormir en esa cama, la desesperación te absorbe \n"           "Sin comida, ni compañia ni sueño.\n"
              "Finalmente decides suicidarte.\n"
              "Has muerto\n"
              "- FIN DEL JUEGO -")
        exit()

    else:
        print(texto_error)
        exit()

elif decision_celda == "D":
    print("\nDecides que la mejor opción es volver a dormir.\n"
          "Despiertas 12h mas tarde a causa del hambre, no aparece nadie y no tienes comida.\n"
          "Finalmente decides suicidarte.\n"
          "Has muerto\n"
          "- FIN DEL JUEGO -")
    exit()

else:
    print(texto_error)
    exit()