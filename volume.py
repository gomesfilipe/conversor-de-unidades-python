from conversor import *
from PySimpleGUI import PySimpleGUI as sg

unidades = ['mm3', 'cm3', 'dm3', 'm3', 'dam3', 'hm3', 'km3']
valorInicial = 0
valorFinal = 0
undInicial = 'm3'
undFinal = 'm3'

sg.theme('BlueMono')

layout = [
    [sg.Text('Converter'), sg.InputText(size=(20,1)), sg.Combo(unidades, default_value='m2'), sg.Text('para'), sg.Combo(unidades, default_value='m2'), sg.Button('Converter')],
    [sg.Text(valorInicial, key='valor-inicial', size=(20,1)), sg.Text(undInicial, key='unidade-inicial', size=(4,1)), sg.Text('equivale a'), sg.Text(valorFinal, key='valor-final', size=(20,1)), sg.Text(undFinal, key='unidade-final', size=(4,1))]
]

window = sg.Window('Conversor de Volumes', layout)

while True:
    evento, valores = window.read()
    
    valorInicial = valores[0]
    undInicial = valores[1]
    undFinal = valores[2]

    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'Converter':
        valorFinal = conversorVolume(valorInicial, undInicial, undFinal, unidades)
    
    if not ehNumero(valorInicial):
        valorInicial = '0'
    
    window['valor-inicial'].update(valorInicial)
    window['valor-final'].update(valorFinal)
    
    window['unidade-inicial'].update(undInicial)
    window['unidade-final'].update(undFinal)

window.close()
