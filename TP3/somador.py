import sys
import re

def processar_palavra(palavra, somador, res, iguais):
    if re.search(r'(?i:on)', palavra):
        somador = True
    elif re.search(r'(?i:off)', palavra):
        somador = False
    elif somador and re.match(r'^[-+]?\d+$', palavra):
        res += int(palavra)
    elif '=' in palavra:
        print(f'{iguais}º "=": {res}')
        iguais += 1
    return somador, res, iguais

def somador(nome):
    somar = True
    res = 0
    iguais = 1

    with open(nome, 'r') as ficheiro:
        for linha in ficheiro:
            palavras = linha.split()
            for palavra in palavras:
                somar, res, iguais = processar_palavra(palavra, somar, res, iguais)
    
def main():
    nome_arquivo = sys.argv[1]
    somador(nome_arquivo)

main()
