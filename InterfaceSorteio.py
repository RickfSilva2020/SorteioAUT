from unittest import defaultTestLoader
import PySimpleGUI as sg 

def Tela_Sorteio():
        # COR DO TEMA
        sg.theme('DarkBlue14')

# LAYOUT
        coluna1 = [
            [sg.Button('Sortear')]
        ]
        coluna2 = [ 
            [sg.Button('Cancel')] 
        ]    
            
        layout = [
            [sg.Text(' ', size=(1, 1))],
            [sg.Text('Digite o nome dos elementos para o sorteio:', size=(45, 2), font= 25)],
            [sg.MLine(default_text='Digite ou cole os elementos aqui:', size= (45,7), key= ('-N1-'))],
            [sg.HSeparator()],
            [sg.Text('Escolha o tipo de Sorteio que você deseja.')],
            [sg.Checkbox(' Sequência', key='-SEQ-'), sg.Text('     ', size=(1, 1)), sg.Checkbox(' Escolha Única', key='-UNI-')],
            [sg.Text('', size=(1, 1))],
            [sg.HSeparator()],
            [sg.Output(size= (45,7))],
            [sg.Push(), sg.Col(coluna1), sg.Col(coluna2)],
                    
        ]
        
        janela = sg.Window('Sorteio', layout= layout, finalize= True)
        
         