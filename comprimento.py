from conversor import *
from PySimpleGUI import PySimpleGUI as sg

unidades = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
valorInicial = 0, valorFinal = 0, undInicial = 'm', undFinal = 'm'

sg.theme('BlueMono')

layout = [
    [sg.Text('Converter'), sg.InputText(size=(20,1)), sg.Combo(unidades, default_value='m'), sg.Text('para'), sg.Combo(unidades, default_value='m'), sg.Button('Converter')],
    [sg.Text(valorInicial, key='valor-inicial', size=(20,1)), sg.Text(undInicial, key='unidade-inicial', size=(3,1)), sg.Text('equivale a'), sg.Text(valorFinal, key='valor-final', size=(20,1)), sg.Text(undFinal, key='unidade-final', size=(3,1))]
]

window = sg.Window('Conversor de Comprimentos', layout)

while True:
    evento, valores = window.read()
    
    valorInicial = valores[0], undInicial = valores[1], undFinal = valores[2]

    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'Converter':
        valorFinal = conversorComprimento(valorInicial, undInicial, undFinal, unidades)
    
    if not ehNumero(valorInicial):
        valorInicial = '0'
    
    window['valor-inicial'].update(valorInicial)
    window['valor-final'].update(valorFinal)
    
    window['unidade-inicial'].update(undInicial)
    window['unidade-final'].update(undFinal)

window.close()
