from conversor import *
from PySimpleGUI import PySimpleGUI as sg

if __name__ == '__main__':
    result = 0
    unidadesComprimento = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
    unidadesArea = ['mm2', 'cm2', 'dm2', 'm2', 'dam2', 'hm2', 'km2']
    unidadesVolume = ['mm3', 'cm3', 'dm3', 'm3', 'dam3', 'hm3', 'km3']
    unidadesSelecionadas = []
    sg.theme('BlueMono')

    layout = [ 
        [sg.Text('Grandeza'), sg.Combo(['Comprimento', 'Área', 'Volume'], enable_events=True)], 
        [sg.InputText(), sg.Combo(unidadesSelecionadas, enable_events=True, key='-UNIDADEENTRADA-')],
        [sg.Text('equivale a')],
        [sg.Text(result, key='-RESULT-'), sg.Combo(unidadesSelecionadas, enable_events=True, key='-UNIDADESAIDA-'), sg.Button('Converter')]
    ]

    janela = sg.Window('Conversor de unidades', layout)

    while True:
        evento, valores = janela.read()
        grandeza = valores[0]
        numberToConvert = valores[1]
        undInicial = valores['-UNIDADEENTRADA-']
        undFinal = valores['-UNIDADESAIDA-']
        
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 0:
            if grandeza == 'Comprimento': 
                unidadesSelecionadas = unidadesComprimento
            elif grandeza == 'Área': 
                unidadesSelecionadas = unidadesArea
            elif grandeza == 'Volume':
                unidadesSelecionadas = unidadesVolume
        
        elif evento == 'Converter':
            if grandeza == 'Comprimento': 
                result = conversorComprimento(numberToConvert, undInicial, undFinal, unidadesSelecionadas)
            elif grandeza == 'Área': 
                result = conversorArea(numberToConvert, undInicial, undFinal, unidadesSelecionadas)
            elif grandeza == 'Volume':
                result = conversorVolume(numberToConvert, undInicial, undFinal, unidadesSelecionadas)

        
        janela['-UNIDADEENTRADA-'].update(values=unidadesSelecionadas)
        janela['-UNIDADESAIDA-'].update(values=unidadesSelecionadas)
        janela['-RESULT-'].update(result)
        print('result', result)
        print('valores', valores)    
        print('evento', evento)
    
    janela.close()


# 'mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km'