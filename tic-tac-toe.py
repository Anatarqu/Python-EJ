import PySimpleGUI as sg      

PLAYER_ONE = "X"
PLAYER_TWO = "O"

current_player = PLAYER_ONE

deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

winner_plays = [[0,1,2],[3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],[0,4,8], [2,4,6]]

layout = [[sg.Button("", key="-0-", size=(7,5)), 
           sg.Button("", key="-1-", size=(7,5)), 
           sg.Button("", key="-2-", size=(7,5))],
         [sg.Button("",key="-3-", size=(7,5)), 
          sg.Button("", key="-4-", size=(7,5)), 
          sg.Button("", key="-5-", size=(7,5))],
         [sg.Button("", key="-6-", size=(7,5)), 
          sg.Button("", key="-7-", size=(7,5)), 
          sg.Button("", key="-8-", size=(7,5))],
         [sg.Text("", key="-WINNER-")],
         [sg.Button("He Terminado", key="-OK-")]]

window = sg.Window("Demo", layout)
game_end = False

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == "-OK-":
    break

  if window.Element(event).ButtonText == "" and not game_end:
     index = int(event.replace ("-",""))
     deck[index] = current_player
     window.Element(event).Update(text=current_player)

     for winner_play in winner_plays:
       if deck[winner_play[0]] == deck[winner_play[1]] != deck [winner_play[2]] == 0:
          if deck[winner_play[0]] == PLAYER_ONE:
            print("El Jugador 1 ha ganado!!")
          else:
            print("El Jugador 2 ha ganado!!")
          game_end = True
         
     if 0 not in deck:
        print("Juego Terminado!")
        game_end = True
       
     if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
     else:
        current_player = PLAYER_ONE
  
window.close()
  
  

