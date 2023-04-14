from jogadores import *
from fileshabilidades.habilidades import Habilidades
from credenciais.entradas import Entradas
from credenciais.pesquisa import Pesquisa
import os

'''INICIAR A MODULAR O MAIN'''

while True:
    print("Bem vindo ao nosso sistema")
    print ("AVISO!!!\n SEMPRE QUE A OPÇÃO FOR SEGUIDA DE (*) A OPÇÃO ESTÁ INDISPONIVEL")
    enter = int(input("Escollha uma das opções para prosseguir\n(1)Iniciar jogo*\n(2)Consultar jogador\n(3)Cadastrar Jogador*\n(4)Sair\nOpção: "))
    
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
        op = entry.pesquisa_por_id()
        op

        if op == False:
            
            limpar.limpar()
            print("Jogador não encontrado!\nEscolha uma opção!\n")
            op2 = int(input("(1)Cadastrar Jogador\n(2)sair"))
            limpar.limpar()
            
            if op2 == 1:
                limpar
                entradacadastro = Entradas()
                entradacadastro.charmar()
                limpar
                j = Jogador(entradacadastro.nome_saida(), entradacadastro.get_nascimento(), 'NULL', entradacadastro.id_saida())
                print(j.nome)
                print(j._nascimento)
                print(j._notas)
                print(j._id)

        fim = input("Pressione enter para continuar")
        os.system("cls")
        break       
        
    elif enter == 3:
        print("Basicamente cadastrar um jogador")
        '''Cadastrar jogador e apagar também'''
        pass
    else:
        break
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