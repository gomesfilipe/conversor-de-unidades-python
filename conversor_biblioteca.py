def ehNumero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def conversorComprimento(valor, undInicial, undFinal, unidadesComprimento):
    if ehNumero(valor):
        valor = float(valor)
        distancia = unidadesComprimento.index(undInicial) - unidadesComprimento.index(undFinal)
        return valor * 10 ** distancia
    
    return 0

def conversorArea(valor, undInicial, undFinal, unidadesArea):
    if ehNumero(valor):
        valor = float(valor)
        distancia = unidadesArea.index(undInicial) - unidadesArea.index(undFinal)
        return valor * 10 ** (2 * distancia)
    
    return 0

def conversorVolume(valor, undInicial, undFinal, unidadesVolume):
    if ehNumero(valor):
        valor = float(valor)
        distancia = unidadesVolume.index(undInicial) - unidadesVolume.index(undFinal)
        return valor * 10 ** (3 * distancia)

    return 0

def conversorGenerico(valor, undInicial, undFinal, unidades, funcao):
    return funcao(valor, undInicial, undFinal, unidades)