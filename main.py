from jogadores import *
from fileshabilidades.habilidades import Habilidades
from credenciais.entradas import Entradas
from credenciais.pesquisa import Pesquisa
import os

'''INICIAR A MODULAR O MAIN'''

while True:
    print("Bem vindo ao nosso sistema")
    print ("AVISO!!!\n!!!SEMPRE QUE A OPÇÃO FOR SEGUIDA DE (*) A OPÇÃO ESTÁ INDISPONIVEL!!!")
    enter = int(input("Escollha uma das opções para prosseguir\n(1)Iniciar jogo*\n(2)Consultar jogador\n(3)Cadastrar Jogador\n(4)Sair\nOpção: "))
    
    limpar = Pesquisa()
    limpar.limpar()

    if enter == 1:
        print("Nessesario iniciar jogo")
        '''Iniciar jogo chamando times, necessario informar a quantidade de jogadores e após começar a definir times
           nesse meio é necessario que sempre que for procurar um jogador pelo nome consiga a opção de consultar o jogador antes de adicionar o 
           jogador e após escolher se deseja adicionar ou não
        '''
        pass

    elif enter == 2 :
       
        limpar.limpar()
        print("Consultar jogador:")
        '''Pode fazer a mesma função de iniciar jogo, só que nessa você consegue editar as informações do jogador'''
        entry = Pesquisa()
        
        limpar.limpar()

        if not entry.p():      
            print("Jogador não encontrado!\nEscolha uma opção!\n")
        
        else:
            '''entregar informações do jogador'''
            pass

        fim = input("Pressione enter para continuar")
        os.system("cls")
        break       
        

    elif enter == 3:
        print("Basicamente cadastrar um jogador")
        '''Cadastrar jogador e apagar também'''
        op2 = int(input("(1)Cadastrar Jogador\n(2)Apagar jogador"))
        limpar.limpar()
            
        if op2 == 1:
            limpar
            entradacadastro = Entradas()
            entradacadastro.charmar()
           
            j = Jogador(entradacadastro.nome_saida(), entradacadastro.get_nascimento(), 'NULL', entradacadastro.id_saida())
            print(f'{j.nome}, {j._nascimento}, {j._notas}, {j._id}')

            j.cadastro()
            limpar.limpar()
        
        elif op2 ==2:
            
            apagarcadastro = Entradas()
            apagarcadastro.charmar()
            pesquisarcadastro = Pesquisa()
            pesquisarcadastro.pesquisa_por_id = apagarcadastro.id_saida()
            j = Jogador(0, 0, 0, apagarcadastro.id_saida())

            j.apagar()
            limpar.limpar()

    elif enter == 4:
        break

    limpar.limpar()
'''
e = Entradas()

e.charmar()
j = Jogador(e.nome_saida(), e.get_nascimento(), "91", e.id_saida())
h = Habilidades(j.nome, j._nascimento, j._notas, j._id, "akaka")
#h.criarhabilidades()

os.system('cls')
print(f'Nome: {h.nome}')
print(f'ID: {h._id}')
print(f'Nascimento: {h._nascimento}')

n = int(input("Escolha uma opção:\n(1)Consultar Jogador\n(2)Habilidades"))

if n == 1:
    print(j.nome)

elif n == 2:
    h.criarhabilidades()

CRIAR ARQUIVOS PARA REGISTRO DO JOGADORES E CONSULTAR ANTES DE ENTRAR

h.modificarhabilidades()

p = Pesquisa()

p.pesquisa_por_id()


exemplo de recebimento tratamento de erros
if e.nome_saida() == False:
    print("not name")
else:
    print("erro inesperado")
'''