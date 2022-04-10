from PySimpleGUI import PySimpleGUI as sg
from length import LengthConverter
from area import AreaConverter
from volum import VolumConverter
from convert import ConvertWindow

class initialWindow:
    def __init__(self):
        sg.theme('BlueMono')
        self.msg = sg.Text('Choose the Converter:', background_color='white')
        self.length = sg.Button('Length Converter', )
        self.area = sg.Button('Area Converter')
        self.volum = sg.Button('Volum Converter')

        # self.length_converter = ConvertWindow(LengthConverter())
        # self.area_converter = ConvertWindow(AreaConverter())
        # self.volum_converter = ConvertWindow(VolumConverter())

        self.layout = [
            [self.msg],
            [self.length],
            [self.area],
            [self.volum]
        ]

    def run_event(self, event):
        if event == 'Length Converter':
            length_converter = ConvertWindow(LengthConverter())
            length_converter.run_converter()
            # self.length_converter.run_converter()

        elif event == 'Area Converter':
            area_converter = ConvertWindow(AreaConverter())
            area_converter.run_converter()

        elif event == 'Volum Converter':
            volum_converter = ConvertWindow(VolumConverter())
            volum_converter.run_converter()

    def run_initial_window(self):
        window = sg.Window('Unit Converter', self.layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break 
            else:
                self.run_event(event)

        window.close()

initial_window = initialWindow()
initial_window.run_initial_window()
