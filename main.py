from modulos.sistema import *

import os
import time

print("Bem vindo ao nosso sistema")

while True:
    
    enter = int(input("Escollha uma das opções para prosseguir\n(1)Iniciar EVENTO\n(2)GESTÃO DE JOGADORES\n(3)Sair\nOpção: "))
    
    #no final de cada jogo deve-se ser calculado todas as funcionalidades de notas, habilidades e etc.
    system = Sistema()
    system.limpar() 
    system.cor()


    if enter == 1:
        
        initevento = Evento()
        e = Entradas()
        p = Pesquisa()
        condit = bool

        print("Evento Iniciado!\n")
        initevento.quantidade_do_evento()

        print("Insira o id de todos os jogadores: ")
        
        for jogador in range(initevento.quantidadetotal):
            e.eid_entrada()
            if p.pesquisa_por_id(e.eid):
                initevento.jogadores.append(e.eid)
                condit = True
            else: 
                print('ID INEXISTENTE\n INSIRA UM ID EXISTENTE')
                e.eid_entrada()
                condit = False
                

        if condit == True:   
            initevento.nome_dos_jogadores()
        else:
            print(f'Lista de jogadores digitados por id  {initevento.jogadores}')
        #USAR CLASSE ENTRADAS PARA REGISTRAR CONFERIR JOGADORES NÃO EXISTENTES
        
        
        '''iNICIAR EVENTO, Deve cadastrar todos o jogadores presentes, definir quantidade de jogadores por time'''
        '''Iniciar jogo chamando times, necessario informar a quantidade de jogadores e após começar a definir times
           nesse meio é necessario que sempre que for procurar um jogador pelo nome consiga a opção de consultar o jogador antes de adicionar o 
           jogador e após escolher se deseja adicionar ou não
        '''
        break

    #UNIR CONSULTAR DE JOGADOR E GESTÃO DE JOGADORES NA MESMA PAGINA
    
    elif enter == 2:

        print("GESTÃO DE JOGADORES")
        '''Cadastrar jogador e apagar também'''
        op2 = int(input("(1)Cadastrar Jogador\n(2)Apagar jogador\n(3)Consultar Jogador\nOpção: "))
        system.limpar()
            
        if op2 == 1:
            #criar pasta exclusiva para jogadores
            entradacadastro = Entradas()
            entradacadastro.charmar()
           
            j = Jogador(entradacadastro.nome_saida(), entradacadastro.get_nascimento(), 'NULL', entradacadastro.id_saida())
        
            
            if j.cadastro():
                print(f'{j.nome}, {j._nascimento}, {j._notas}, {j._id}')
            time.sleep(3)
            system.limpar()
        
        elif op2 ==2:
            '''CRIAR FUNCIONALIDADE PARA PESQUISAR NOME DO JOGADOR E DATA DE NASCIMENTO CASO NÃO LEMBRAR DO ID'''
            e = Entradas()
            e.eid_entrada()
            system.limpar()
            pesquisarcadastro = Pesquisa()
            
            
            j = Jogador(0, 0, 0, e.id_saida())

            j.apagar()
            time.sleep(3)
            system.limpar()

        elif op2 ==3 :
             
            system.limpar()
            print("Consultar jogador:")
            '''Pode fazer a mesma função de iniciar jogo, só que nessa você consegue editar as informações do jogador'''
            entradas = Entradas()
            entradas.eid_entrada()
            pesquisa = Pesquisa()
            
            system.limpar()

            while True:

                p = pesquisa.pesquisa_por_id(entradas.id_saida())
                
                if not p:      
                    op = input("Deseja continuar pequisa? (S)")
                    if op == 'S':
                        continue
                    else: 
                        break
                    
                else:
                    '''entregar informações do jogador'''
                    break

            fim = input("Pressione enter para continuar")
            os.system("cls")


    elif enter == 4:
        break   

    system.limpar()
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