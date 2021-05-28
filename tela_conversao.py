from biblioteca import *
from PySimpleGUI import PySimpleGUI as sg

def telaConversao(funcao, unidades, undInicial, undFinal, titulo):
    valorInicial = 0
    valorFinal = 0

    sg.theme('BlueMono')

    layout = [
        [sg.Text('Converter'), sg.InputText(size=(20,1)), sg.Combo(unidades, default_value=undInicial), sg.Text('para'), sg.Combo(unidades, default_value=undFinal), sg.Button('Converter')],
        [sg.Text(valorInicial, key='valor-inicial', size=(20,1)), sg.Text(undInicial, key='unidade-inicial', size=(4,1)), sg.Text('equivale a'), sg.Text(valorFinal, key='valor-final', size=(20,1)), sg.Text(undFinal, key='unidade-final', size=(4,1))]
    ]

    window = sg.Window(titulo, layout)

    while True:
        evento, valores = window.read()
        
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'Converter':
            valorInicial = valores[0]
            undInicial = valores[1]
            undFinal = valores[2]
            valorFinal = funcao(valorInicial, undInicial, undFinal, unidades)
        
        if not ehNumero(valorInicial) or not estaNaLista(undInicial, unidades) or not estaNaLista(undFinal, unidades):
            valorInicial = ''
            valorFinal = ''
            undInicial = ''
            undFinal = ''

        window['valor-inicial'].update(valorInicial)
        window['valor-final'].update(valorFinal)
        
        window['unidade-inicial'].update(undInicial)
        window['unidade-final'].update(undFinal)

    window.close()
