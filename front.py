from PySimpleGUI import PySimpleGUI as sg
from modulos.pesquisa import Pesquisa

class Tema:

    def __init__(self):
        sg.theme('Dark Blue')
        layout = [
            [sg.Text('Escolha sua opção')],
            [sg.Input(key='Input')],
            [sg.Button('Cadastro'), sg.Button('Consulta'), sg.Button('Sair')]
        ]
        self.main = sg.Window('Iniciar', layout=layout, finalize=True)

        layout2 = [
            [sg.Text('Insira seu nome')],
            [sg.Input(key='Nome2')],
            [sg.Button('Entrar'), sg.Button('Sair')]
            
        ]
        self.cadastro = sg.Window('Cadastro', layout=layout2, finalize=True)

        layout3 = [
            [sg.Text('Insira o nome do jogador')],
            [sg.Text('Nome'), sg.Input()],
            [sg.Button('Enviar'), sg.Button('Cancelar')],
        ]
        self.consulta = sg.Window('Consulta', layout=layout3, finalize=True)


    def iniciar(self):
        janelamain = self.main

        while True:
            event, values = janelamain.read() # type: ignore

            if event == 'Cadastro':
                janelamain.hide()
                janela_atual =  self.cadastro
                janela_atual.un_hide()
            
            elif event == 'Consulta':
                janelamain.hide()
                janela_atual = self.consulta 
                janela_atual.un_hide()
            
            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelamain.close()
                break

        

t = Tema()
t.iniciar()




