from PySimpleGUI  import PySimpleGUI as sg


sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key= 'usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar? ')],
    [sg.Button('Entrar')]
]

#janela

janela = sg.Window('Tela de login', layout)

#eventos

while True:
    
    eventos, valores = janela.read() # type: ignore
    
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'arthur' and valores ['senha'] == '12345':
            print('Bem vindo')

