from tkinter import OFF
from InterfaceSorteio import *
from CodigoSorteio import *
import random as rd
from time import sleep as sl





Tela_Sorteio()

while True:
    janela, evento, valores = sg.read_all_windows()

    if evento == sg.WIN_CLOSED or evento == 'Cancel':
        break

    if evento == 'Sortear':
        
        lista = []
        n = str(valores['-N1-']).upper().replace(' ', '_')
        seq = valores['-SEQ-']
        uni = valores['-UNI-']
        
        

        lista = []
        n1 = n.split()

        for i in n1:
            lista.append(i)
        print(f'Os elemanentos digitados foram {lista}.')
        
        
        c = 0
        if uni == True and seq == False:

            res = rd.choice(lista)
            sg.popup_quick_message('Processando!!')
            sl(2)
            sg.popup_quick_message('O SORTEADO FOI', font= 40)
            sl(2)
            sg.popup_no_buttons((res), font=(
                'Calibri', 80),  background_color='black')
            break
        
        
        if uni == False and seq == True:
            
            res = rd.sample(lista, len(lista))
            for e in res:
                print(e)
                print('Clique em ok para o próximo')
                c += 1
                sg.popup_quick_message('Processando!!')
                sl(2)
                sg.popup_quick_message('O SORTEADO FOI', font= 40)
                sl(2)
                sg.popup((f'{c}º - {e}'), font=(
                    'Calibri', 25),  background_color='black')
            break
        
        else:
            sg.popup_no_buttons('Escolha o tipo de sorteio!!', font=(
                'Calibri', 30))

       
        
