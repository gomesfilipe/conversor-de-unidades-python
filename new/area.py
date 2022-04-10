class AreaConverter:
    def __init__(self):
        self.name = 'Area Converter'
        self.scale = {
            'mm²': 0.000001,
            'cm²': 0.0001,
            'dm²': 0.01,
            'm²': 1,
            'dam²': 100,
            'hm²': 10000, 
            'km²': 1000000
        }

        self.legend = {
            'mm²': 'square millimeter',
            'cm²': 'square centimeter',
            'dm²': 'square decimeter',
            'm²': 'square meter',
            'dam²': 'square dekameter',
            'hm²': 'square hectometer', 
            'km²': 'square kilometer'
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
        