from tela_conversao import telaConversao
from biblioteca import *
from PySimpleGUI import PySimpleGUI as sg

unidadesComprimento = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
unidadesArea = ['mm2', 'cm2', 'dm2', 'm2', 'dam2', 'hm2', 'km2']
unidadesVolume = ['mm3', 'cm3', 'dm3', 'm3', 'dam3', 'hm3', 'km3']

tituloComprimento = 'Conversor de Comprimentos'
tituloArea = 'Conversor de Áreas'
tituloVolume = 'Conversor de Volumes'

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
        funcao = conversorComprimento
        unidades = unidadesComprimento
        undInicial = 'm'
        undFinal = 'm'
        titulo = tituloComprimento
        
    elif evento == 1: # Área
        funcao = conversorArea
        unidades = unidadesArea
        undInicial = 'm2'
        undFinal = 'm2'
        titulo = tituloArea
    
    elif evento == 2: # Volume
        funcao = conversorVolume
        unidades = unidadesVolume
        undInicial = 'm3'
        undFinal = 'm3'
        titulo = tituloVolume

    telaConversao(funcao, unidades, undInicial, undFinal, titulo)

window.close()
