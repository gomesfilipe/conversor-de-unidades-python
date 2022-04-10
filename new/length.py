class LengthConverter:
    def __init__(self):
        self.name = 'Length Converter'
        self.scale = {
            'mm': 0.001,
            'cm': 0.01,
            'dm': 0.1,
            'm': 1,
            'dam': 10,
            'hm': 100, 
            'km': 1000
        }
        
        self.legend = {
            'mm': 'millimeter',
            'cm': 'centimeter',
            'dm': 'decimeter',
            'm': 'meter',
            'dam': 'dekameter',
            'hm': 'hectometer', 
            'km': 'kilometer'
        }

        self.keys = list(self.scale.keys())

    def converter(self, value, fr, to):
        if fr in self.scale and to in self.scale:
            return float(value) * self.scale[fr] / self.scale[to]
        else:
            return ''

    def generate_legend(self):
        legend = ''
        for key in self.legend:
            legend = legend + key + ': ' + self.legend[key] + '\n'
        
        return legend
        
