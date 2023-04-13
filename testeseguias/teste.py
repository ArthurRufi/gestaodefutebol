def set_nascimento():
        
        day = input("Insira o DIA de nascimento")
        mounth = input("Insira o mês de nascimento")
        years = input("Insira o Ano de nascimento")

        while True:
            if len(day) == 2 and len(mounth) == 2 and len(years):
                break
            else:
                print("Insira Novamente as credenciais")
                day = input("Insira o DIA de nascimento")
                mounth = input("Insira o mês de nascimento")
                years = input("Insira o Ano de nascimento")
        
        while True:
            if not day.isdigit():
                print("Dia invalido")
                day = input("Insira o DIA de nascimento")

            elif not mounth.isdigit():
                print("Mês Invalido")
                mounth = input("Insira o mês de nascimento")
            elif not years.isdigit():
                print("Ano invalido")
                years = input("Insira o Ano de nascimento")
            else:
                print("OK")
                break


        '''TRATAR AS ENTRADAS'''
        date = (f'{day}/{mounth}/{years}')
        print(date)


set_nascimento()