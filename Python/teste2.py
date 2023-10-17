try:
    valor = float(input("Digite o valor do depósito: "))
except ValueError:
    print("Encerrando o programa......")
else:
    if valor > 0:
        saldo = valor
        print("Depósito realizado com sucesso!")
        print("Saldo atual: R${:.2f}".format(saldo))
    elif valor == 0:
        print("Valor inválido! Digite um valor maior que zero.")
    else:
        print("Encerrando o programa......")