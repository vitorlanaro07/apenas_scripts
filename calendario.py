def e_bissexto(ano):
    ano_verificacao = list(str(ano))
    digitos = len(ano_verificacao)-1

    if ano_verificacao[digitos] == "0" and ano_verificacao[digitos-1] == "0":
        resto = ano % 400
        if(resto == 0):
            return True
        else:
            return False
    else:
        resto = ano % 4
        if (resto == 0):
            return True
        else:
            return False

def get_dias(tipo_ano):
    if tipo_ano == True:
        return 30
    else:
        return 29

def calendario(tipo_ano):
    mes_dias = [["Janeiro",range(1,32)],["Fevereiro",range(1,get_dias(tipo_ano))],["Março",range(1,32)],["Abril",range(1,31)],
                ["Maio",range(1,32)],["Junho",range(1,31)],["Julho",range(1,32)],["Agosto",range(1,32)],
                ["Setembro",range(1,31)],["Outubro",range(1,32)], ["Novembro",range(1,31)],["Dezembro",range(1,32)]]

    for mes, dias in mes_dias:
        print("\n       {0}".format(mes))
        dia_da_semana = 1
        ultimo_dia = max(dias)

        for dia in dias:
            if dia == ultimo_dia:
                print("{:02d}".format(dia))
            elif dia_da_semana < 7:
                print("{:02d}".format(dia), end=" ")
                dia_da_semana += 1
            elif dia_da_semana == 7:
                print("{:02d}".format(dia), sep=" ")
                dia_da_semana = 1

if(__name__ == "__main__"):
    bissexto = e_bissexto(int(input("Qual ano você deseja ver o calendario:")))
    calendario(bissexto)