from asyncio.windows_events import NULL
from operator import le
from os import system
from turtle import clear
import requests
import json


# Validar quando a palavra não é encontrada
# Continuar pesquisando diferentes palavras
# Dividir em módulos
# Corrigir a descrição
def consultar_dicio():
    print("##########################################################")
    response = requests.get("https://api.dicionario-aberto.net/word/fasfuqiwfsa").text
    while len(response) == 2:
        palavra = str(input("Qual palavra você deseja saber o significado: ")).casefold()
        url = f"https://api.dicionario-aberto.net/word/{palavra}"
        response = requests.get(url).text
        if len(response) == 2:
            print("Palavra não encontrada!!")

    response_info = json.loads(response)

    palavra = []
    word_id = []
    descricao = str
    
    for x in response_info:
        palavra = x['word']
        word_id = x['word_id']
        descricao = x['xml']

    print("##########################################################")
    print(f'Id_da_Palavra: {word_id} \nPalavra: {str(palavra).capitalize()}')

    for x in descricao:
        inicial = descricao.find("<def>")
        final = descricao.find("</def>")

    print("##########################################################")
    print("\nDescrição: \n\n"+descricao[inicial+6:final])
    print("##########################################################")

respo = ''
while respo != 'sim' or respo != 'nao': 
    respo = ''   
    respo = input("Deseja pesquisar uma palavra(sim/nao): ")
    if (respo == 'nao'):
        break
    if (respo == 'sim'):
        consultar_dicio()

    
    