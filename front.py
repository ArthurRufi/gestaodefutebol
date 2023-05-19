from PySimpleGUI import PySimpleGUI as sg
from modulos.pesquisa import Pesquisa
import time

class Tema:

    def __init__(self):

        pass


    def iniciar(self):
        janelamain = self.main
        
        

    def janela1(self):
        sg.theme('Dark Blue')
        layout = [
            [sg.Text('Escolha sua opção')],
            [sg.Radio('Evento', 'g', key='Evento')],
            [sg.Radio('Gestão de jogadores', 'g', key='Gestão')],
            [sg.Button('Enviar'), sg.Button('Sair')]
        ]
        self.main = sg.Window('Iniciar', layout=layout, finalize=True)
        
        janelamain = self.main

        while True:
            event, values = janelamain.read() # type: ignore

            if event == 'Enviar':

                if values['Evento'] == True:
                    janelamain.close()
                    return '1'
                    
                elif values ['Gestão'] == True:
                    janelamain.close()
                    return '2'
                
            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelamain.close()
                break

        janelamain.close()


    def interface_pesquisa(self):
        layout2 = [
            [sg.Text('Insira o id do jogador')],
            [sg.Input(key='Nome2')],
            [sg.Button('Entrar'), sg.Button('Sair')]
            
        ]

        self.pesquisa = sg.Window('Pesquisa', layout=layout2, finalize=True)

        janelaatual = self.pesquisa
        event, values = janelaatual.read() # type: ignore

        if event == 'Entrar':
            
            return values
        elif event == 'Sair' or event == sg.WIN_CLOSED:
            janelaatual.close()
                

    def cadastrar(self):
        sg.theme('LightYellow')
        layout3 = [
                [sg.Text('Insira os dados do jogador')],
                [sg.Text('Nome', size=20), sg.Input(key= 'Name')],
                [sg.Text('ID', size=20), sg.Input(key= 'id')],
                [sg.Text('Nascimento', size=20), sg.Input(key= 'nascimento')],
                [sg.Button('Enviar'), sg.Button('Sair')],
            ]

        self.consulta = sg.Window('Cadastro', layout=layout3, finalize=True)

        janelamain = self.consulta

        while True:
            event, values = janelamain.read() # type: ignore

            if event == 'Enviar':

                if values['Name'] != None and values['id'] != None and values['nascimento'] != None:
                    print (values)
                    return '1'
                    
                elif values ['Gestão'] == True:
                    return '2'
                
            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelamain.close()
                break

        janelamain.close()





