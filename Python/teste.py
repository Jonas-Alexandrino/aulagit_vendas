saldo_atual = float(input("Escreva o saldo atual do colaborador: "))
valor_deposito = float(input("Escreva do valor do depósito: "))
valor_retirada = float(input("Escreva o valor de retirada: "))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual = saldo_atual + valor_deposito - valor_retirada

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print("Saldo atualizado na conta: {:.1f}".format(saldo_atual))