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
legendaArea = 'mm: milímetros quadrados\ncm: centímetros quadrados\ndm: decímetros quadrados\nm: metros quadrados\ndam: decâmetros quadrados\nhm: hectômetros quadrados\nkm: quilômetros quadrados'
legendaVolume = 'mm: milímetros cúbicos\ncm: centímetros cúbicos\ndm: decímetros cúbicos\nm: metros cúbicos\ndam: decâmetros cúbicos\nhm: hectômetros cúbicos\nkm: quilômetros cúbicos'

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
