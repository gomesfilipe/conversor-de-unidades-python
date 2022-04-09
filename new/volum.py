class VolumConverter:
    def __init__(self):
        self.name = 'Volum Converter'
        self.scale = {
            'mm³': 0.000000001,
            'cm³': 0.000001,
            'dm³': 0.001,
            'm³': 1,
            'dam³': 1000,
            'hm³': 1000000, 
            'km³': 1000000000
        }

        self.legend = {
            'mm³': 'cubic millimeter',
            'cm³': 'cubic centimeter',
            'dm³': 'cubic decimeter',
            'm³': 'cubic meter',
            'dam³': 'cubic dekameter',
            'hm³': 'cubic hectometer', 
            'km³': 'cubic kilometer'
        }

        self.keys = list(self.scale.keys())

    def converter(self, value, fr, to):
        if fr in self.scale and to in self.scale:
            return float(value) * self.scale[fr] / self.scale[to]
        else:
            return ''
