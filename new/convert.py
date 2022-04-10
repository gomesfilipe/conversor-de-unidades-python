from pydoc import visiblename
from PySimpleGUI import PySimpleGUI as sg
from length import LengthConverter
from area import AreaConverter
from volum import VolumConverter
import re
import pyperclip as pp

class ConvertWindow:
    def __init__(self, converter):
        sg.theme('BlueMono')

        self.converter = converter
        self.result = ''
        self.conv =      sg.Text('Convert')
        self.input =     sg.InputText(size=(24,1))
        self.unit_from = sg.Combo(self.converter.keys, default_value=self.converter.keys[3])
        self.to =        sg.Text('to')
        self.unit_to =   sg.Combo(self.converter.keys, default_value=self.converter.keys[3])
        self.convert =   sg.Button('Convert', size=(39,1))
        self.reset =     sg.Button('Reset', size=(6,1))
        self.visor =     sg.Text(self.result, size=(39,1), justification='center', background_color='white', text_color='black', key='visor')
        self.copy =      sg.Button('Copy', size=(6,1))
        self.checkbox = sg.Checkbox('Legend', enable_events=True)
        self.legend = sg.Text(self.converter.generate_legend(), visible=False, background_color='white', key='legend')
        self.visible = False

        self.layout = [
            [self.conv, self.input, self.unit_from, self.to, self.unit_to],
            [self.convert, self.reset],
            [self.visor, self.copy],
            [self.checkbox],
            [self.legend]
        ] 

    def run_event(self, event, values):
        if event == 'Convert':
            if bool(re.match('^\d+(\.\d+)?$', values[0])):
                result = self.converter.converter(values[0], values[1], values[2]) # 0 é o número, 1 é unidade inicial e 2 é unidade final
                self.result = str(result)
        
        if event == 'Reset':
            self.result = ''

        elif event == 'Copy':
            pp.copy(str(self.result))

    def run_converter(self):
        window = sg.Window(self.converter.name, self.layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == 3: # legenda
                self.visible = not self.visible
                window['legend'].update(visible=self.visible)
            
            else:
                self.run_event(event, values)
            
            window['visor'].update(self.result)
        
        window.close()
            