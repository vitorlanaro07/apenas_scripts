def chamada():
    tema = "Zombi"
    dia = input("Dia: ")
    mes = input("Mês: ")
    ano = input("Ano: ")
    infectatos = input("Numero de pessoas infectadas: ")
    conjuge = input("Conjuge: ")
    parte_corpo = input("Parte do corpo: ")

    textoConcatenado = f"O tema é {tema}.{dia} de {mes} de {ano}, havia eclodido um apocalipse zumbi, {infectatos} haviam sido infectadas.\
        Meu {conjuge} havia sido infectado também, os zumbis morderam seu/sua {parte_corpo}."

    print(textoConcatenado)
