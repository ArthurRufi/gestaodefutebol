class Jogador:
    def __init__(self, nome, nascimento, notas, iden):
        self._nome =  nome
        self._nascimento = nascimento
        self._notas= notas
        self._id = iden
        

class Pontos(Jogador):
    def __init__(self, tops, cabecapoints, pontosproprios, jogador):
        self._toptree = tops
        self._cabeca = cabecapoints
        self._pontos = pontosproprios
        self._idenfication =  jogador
        

        print (self._cabeca)
    

class Habilidades():
    def __init__(self, jogador, conjunto):
        
        self._jogador = jogador
        self._conjunto = conjunto

        
    def habilidadesdetalhadas(self):
        
        habilidadesdojogador ={"Ataque": 0, "Defesa": 1, "Passe": 2, "Velocidade": 3, "Inteligencia": 4, "Visão": 5, "Resistencia": 6, "Drible": 7}

        for k, r in habilidadesdojogador.items():
            print(r)
        '''
        Receber habilidades e retornar um dicionario com as informações tratadas
        ou Receber já um dicionario e retornar as informações tratadas
                     habilidades: ataque, defesa, passe, velocidade, inteligencia, visão de jogo, resistencia, drible.

        '''
        pass