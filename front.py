from PySimpleGUI  import PySimpleGUI as sg

class Tema:
   
    def __init__(self):
        sg.theme('Dark Blue')
        layout = [
            [sg.Text("Insira o nome do jogador")],
            [sg.Button('Obter'), sg.Button('Cancelar')],
            
        ]
        janela = sg.Window("Sistema", layout)
        while True:
            evento, valores = janela.read() # type: ignore
            if evento ==sg.WIN_CLOSED or evento == 'Cancelar':
                janela.close()
                break
                
    
    def iniciar(self):
        pass

t= Tema()