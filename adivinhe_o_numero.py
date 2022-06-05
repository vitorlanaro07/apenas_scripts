import random

# Sortear um numero
# Dar uma dica
#
inicial = -1
limite = -2
valor = -1

while inicial < 0:
    inicial = int(input("Entre com um valor inicial: "))

while limite < inicial:
    limite = int(input("Entre com um valor limite: "))

sorteado = random.randrange(inicial, limite)

print(f"Foi sorteado um valor entre ({inicial}-{limite}) \n")

tentativas = 0

while valor != sorteado:
    valor = int(input("Adivinhe qual numero foi sorteado: "))
    tentativas += 1
    if valor < sorteado:
        print("Valor menor que o sorteado!! Escolha um Maior")
    elif valor > sorteado:
        print("Valor maior que o sorteado!! Escolha um Menor")
    elif valor == sorteado:
        print(f"Você acertou, o valor sorteado foi: {sorteado}")
        print(f"Foi necessario {tentativas} tentativas para acertar")

input()
