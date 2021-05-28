from conversor_comprimento import telaConversorComprimento
from conversor_volume import telaConversorVolume
from conversor_area import telaConversorArea
from conversor_biblioteca import *
from PySimpleGUI import PySimpleGUI as sg

sg.theme('BlueMono')

layout = [
    [sg.Text('O que você deseja converter?', size=(35,1))],
    [sg.Radio('Comprimento', 'options', enable_events=True), sg.Radio('Área', 'options', enable_events=True), sg.Radio('Volume', 'options', enable_events=True)]
]

window = sg.Window('Conversor de Medidas', layout, text_justification='center', element_justification='center')

while True:
    evento, valores = window.read()

    if evento == sg.WIN_CLOSED:
        break
    elif evento == 0: # Comprimento
        telaConversorComprimento()
    elif evento == 1: # Área
        telaConversorArea()
    elif evento == 2: # Volume
        telaConversorVolume()

window.close()