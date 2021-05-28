def ehNumero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def estaNaLista(und, unidades):
    try:
        unidades.index(und)
        return True
    except ValueError:
        return False

def conversorComprimento(valor, undInicial, undFinal, unidadesComprimento):
    if ehNumero(valor) and estaNaLista(undInicial, unidadesComprimento) and estaNaLista(undFinal, unidadesComprimento):
        valor = float(valor)
        distancia = unidadesComprimento.index(undInicial) - unidadesComprimento.index(undFinal)
        return valor * 10 ** distancia
    
    return 0

def conversorArea(valor, undInicial, undFinal, unidadesArea):
    if ehNumero(valor) and estaNaLista(undInicial, unidadesArea) and estaNaLista(undFinal, unidadesArea):
        valor = float(valor)
        distancia = unidadesArea.index(undInicial) - unidadesArea.index(undFinal)
        return valor * 10 ** (2 * distancia)
    
    return 0

def conversorVolume(valor, undInicial, undFinal, unidadesVolume):
    if ehNumero(valor) and estaNaLista(undInicial, unidadesVolume) and estaNaLista(undFinal, unidadesVolume):
        valor = float(valor)
        distancia = unidadesVolume.index(undInicial) - unidadesVolume.index(undFinal)
        return valor * 10 ** (3 * distancia)

    return 0
