def conversorComprimento(valor, undInicial, undFinal, unidadesComprimento):
    distancia = unidadesComprimento.index(undInicial) - unidadesComprimento.index(undFinal)
    return valor * 10 ** distancia

def conversorArea(valor, undInicial, undFinal, unidadesArea):
    distancia = unidadesArea.index(undInicial) - unidadesArea.index(undFinal)
    return valor * 10 ** (2 * distancia)

def conversorVolume(valor, undInicial, undFinal, unidadesVolume):
    distancia = unidadesVolume.index(undInicial) - unidadesVolume.index(undFinal)
    return valor * 10 ** (3 * distancia)

# if __name__ == '__main__':
#     unidadesComprimento = ['mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']
#     unidadesArea = ['mm2', 'cm2', 'dm2', 'm2', 'dam2', 'hm2', 'km2']
#     unidadesVolume = ['mm3', 'cm3', 'dm3', 'm3', 'dam3', 'hm3', 'km3']
    
#     print('Unidades de comprimento: {}'.format(' '.join(unidadesComprimento)))
#     print('Unidades de area: {}'.format(' '.join(unidadesArea)))
#     print('Unidades de volume: {}'.format(' '.join(unidadesVolume)))

#     conversor = input('\nVoce quer converter comprimento (c), área (a) ou volume (v)? ')
#     valor, undInicial = input('Digite o valor e unidade: ').split()
#     undFinal = input('Para qual unidade voce deseja converter? ')

#     valor = float(valor)

#     if conversor == 'c': valorConvertido = conversorComprimento(valor, undInicial, undFinal, unidadesComprimento) 
#     elif conversor == 'a': valorConvertido = conversorArea(valor, undInicial, undFinal, unidadesArea)
#     elif conversor == 'v': valorConvertido = conversorVolume(valor, undInicial, undFinal, unidadesVolume) 

#     print('{:.2E} {} é igual a {:.2E} {}'.format(valor, undInicial, valorConvertido, undFinal))
