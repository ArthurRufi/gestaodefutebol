from PySimpleGUI  import PySimpleGUI as sg
from modulos.sistema import *

class Tema:
   
    def __init__(self):
        '''sg.theme('Dark Blue')
        layout = [
            [sg.Text("Insira o nome do jogador")],
            [sg.Button('Obter'), sg.Button('Cancelar')],
            
        ]
        '''
       # janela = sg.Window("Sistema", layout)
        '''while True:
            evento, valores = janela.read() # type: ignore
            if evento ==sg.WIN_CLOSED or evento == 'Cancelar':
                janela.close()
                break

            if evento == 'Obter':
                print ("agua")
        '''
    def iniciar(self):
        layout = [
            [sg.Text('Escolha sua opção')],
            [sg.Input()],
            [sg.Button("Escolha")]

        ]

        return sg.Window('Iniciar', layout= layout, finalize= True)
    


t= Tema()

janela1 = t.iniciar()
while True:
    window,event, values =sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED:
        break


    if  window == janela1 and event == 'Escolha':
        print("ok")