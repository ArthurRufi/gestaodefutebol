import os



class Entradas:
    def __init__(self):
        self.enome = ""
        self.eid = ""
        self.nascimento = ""
        self.notas = ""
        #COLOCAR METODO PARA CRIAR O ID AUTOMATICO
        #CRIAR SISTEMA PARA NOTAS
        
    def nome_entrada(self):

        na = input("Insira o nome do jogador: ")
        
        '''tentar inserir um list compreension no para realizar toda a tarefa'''
        '''Fazer o nome sempre ficar letra maiscula'''
        '''Fazer que se o jogador não existir exigir que o usuario cadastre o jogador'''
        while True:
            if not na.isalpha():
                na = input("Insira um nome Valido: ")
            else:
                while True:
                    #Isso não funciona sem nem oq faz, mas deve-se arrumar
                    if not os.path.exists(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{na}.txt'):
                        break
                    else:
                        break
                break
        
        self.enome = na

        return self.enome
        
        

    def eid_entrada(self):

        na = input("Insira o id do jogador: ")

        while True:
            if not na.isdigit():
                na = input("Insira um ID Valido: ")
            else:
                break
        
        self.eid = na

        return self.eid


    def nome_saida(self):

        if self.enome == "":
            return False
        else:
            return self.enome 
        '''Colocar um return FALSE em todas as saidas caso o nome de entrada não exista.'''
    

    def id_saida(self):
        
        if self.eid == "":
            return False
        else:
            return self.eid
            
        
    def set_nascimento(self):
        
        #ARRUMAR ESSA PORCARIA
        day = input("Insira o DIA de nascimento: ")
        mounth = input("Insira o mês de nascimento: ")
        years = input("Insira o Ano de nascimento: ")
        
        while True:
            if not day.isdigit() or int(day) > 31 or int(day) <= 0:
                print("Dia invalido")
                day = input("Insira o DIA de nascimento: ")

            elif not mounth.isdigit() or int(mounth) > 12 or int(mounth) <= 0:
                print("Mês Invalido")
                mounth = input("Insira o mês de nascimento: ")
            elif not years.isdigit() or int(years) <= 1910:
                print("Ano invalido")
                years = input("Insira o Ano de nascimento: ")
            else:
                print("OK")
                break


        '''TRATAR AS ENTRADAS'''
        date = (f'{day}/{mounth}/{years}')
        self.nascimento = date
        
        
    def get_nascimento(self):
        
        if self.nascimento == "":
            return False
        else:
            return self.nascimento


    def set_notas(self):
        #vai receber notas e tratar as mesmas.
        pass

    
    def get_notas(self):
        #retornar as notas como nota ou boolean
        pass

    def charmar(self):
        
        self.nome_entrada()
        self.eid_entrada()
        self.set_nascimento()
        