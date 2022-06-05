from operator import index, le
import requests
import json

#Achar uma palavra aleatória
chamada = requests.get("https://api.dicionario-aberto.net/random").text
chamada = json.loads(chamada)

#Adicionar a uma lista
palavraInList = list(chamada["word"])
#Criar uma sting
palavra = chamada["word"]

#Buscar informações adicionais
url = f"https://api.dicionario-aberto.net/word/{palavra}"
response = requests.get(url).text
response_info = json.loads(response)

for x in response_info:
        dica = x['xml']

for x in dica:
    inicial = dica.find("<def>")
    final = dica.find("</def>")

print("##########################################################")
print("Dica: \n\n"+dica[inicial+6:final])
print("##########################################################")


palRecor = []
new_word = str
indexLetra = 0
check = palavraInList.copy()

for x in palavraInList:
    palRecor.append(" ")

while palRecor != check:
    busca = input("Qual letra você acha que tem na palavra: ")
    for letra in palavraInList:
        if letra == busca:
            indexLetra = palavraInList.index(letra)
            palavraInList.pop(indexLetra)
            palavraInList.insert(indexLetra," ")
            palRecor.pop(indexLetra)
            palRecor.insert(indexLetra, letra)
    print(f"Palavra: {palRecor}")

print(f"Parabéns você acertou, a palavra é: {str(palavra).capitalize()}")

input("< Pressione Enter >")