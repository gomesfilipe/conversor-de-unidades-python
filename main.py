from tela_conversao import telaConversao
from biblioteca import *
from PySimpleGUI import PySimpleGUI as sg

unidadesComprimento = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
unidadesArea = ['mm2', 'cm2', 'dm2', 'm2', 'dam2', 'hm2', 'km2']
unidadesVolume = ['mm3', 'cm3', 'dm3', 'm3', 'dam3', 'hm3', 'km3']

tituloComprimento = 'Conversor de Comprimentos'
tituloArea = 'Conversor de Áreas'
tituloVolume = 'Conversor de Volumes'

legendaComprimento = 'mm: milímetros\ncm: centímetros\ndm: decímetros\nm: metros\ndam: decâmetros\nhm: hectômetros\nkm: quilômetros'
legendaArea = 'mm2: milímetros quadrados\ncm2: centímetros quadrados\ndm2: decímetros quadrados\nm2: metros quadrados\ndam2: decâmetros quadrados\nhm2: hectômetros quadrados\nkm2: quilômetros quadrados'
legendaVolume = 'mm3: milímetros cúbicos\ncm3: centímetros cúbicos\ndm3: decímetros cúbicos\nm3: metros cúbicos\ndam3: decâmetros cúbicos\nhm3: hectômetros cúbicos\nkm3: quilômetros cúbicos'

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
        funcaoConversao = conversorComprimento
        unidades = unidadesComprimento
        undInicial = 'm'
        undFinal = 'm'
        titulo = tituloComprimento
        legenda = legendaComprimento
        
    elif evento == 1: # Área
        funcaoConversao = conversorArea
        unidades = unidadesArea
        undInicial = 'm2'
        undFinal = 'm2'
        titulo = tituloArea
        legenda = legendaArea
    
    elif evento == 2: # Volume
        funcaoConversao = conversorVolume
        unidades = unidadesVolume
        undInicial = 'm3'
        undFinal = 'm3'
        titulo = tituloVolume
        legenda = legendaVolume

    telaConversao(funcaoConversao, unidades, undInicial, undFinal, titulo, legenda)

window.close()
