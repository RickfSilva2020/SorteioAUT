import random as rd




                
                
def sorteio():
    
    n1 = valores['-N1-']
    print(n1)

    lista = []

    while True:
        
        #n1 = str(self.valores['n1'])
        #n1 = str(input('Digite o nome elemento: ')).strip().upper()
        print(n1)
        

        if n1 not in lista:
            lista.append(n1)

            if n1 == 'SAIR':
                lista.pop()

                break
                
        
        else:
            print('O elemento digitado já encontra-se no sorteio\nDigite outro nome.')

    print(lista)
'''
    c = 0
    while True:
        esc = int(input('Escolha a opção de sorteio desejada [ 1/2 ] '))

        if esc == 1:
            esc1 = rd.choice(lista)
            print(esc1)
            break

        elif esc == 2:
            esc2 = rd.sample(lista, len(lista))
            for i in esc2:
                c += 1
                print(f'{c} -- {i}')
                break
        
        else:
            print('Opção inválida, tente novamente!!')
'''

        

       

