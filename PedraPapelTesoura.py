import random

# Eu gero o valor de Pedra, Papel e Tesoura
# Eu faço minha escolha
# Eu ganho ou perco



def play():
    computer = random.choice(["Pedra", "Papel", "Tesoura"])
    user = input("Qual sua escolha (Pedra/Papel/Tesoura): ")

    if(status(computer,user) == True):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("A maquina escolheu {0} e voce {1}".format(computer,user))


def status(computer,user):
    if (user == "Pedra" and computer == "Tesoura"):
        return True 
    elif (user == "Papel" and computer == "Pedra"):
        return True
    elif (user == "Tesoura" and computer == "Papel"):
        return True
    else:
        return False

resp = "sim"
while resp != "nao":
    play()
    resp = input("Você que continuar jogando? (sim/nao)")
