print("hello world")

print ("oi, seja bem vindo ao curso de python")

#listas
frutas=["maça", "laranja","banana", "pera", "uva"]
print(frutas[1])
print(frutas[-1])
print(frutas[1:])
for frutas in frutas:
    print (frutas)


for indice, frutas in enumerate (frutas):
    print (f"{indice}:{frutas}")

#tuplas
numeros = tuple([1, 2, 3, 4])

#variaveis, funções de entrada e saida
age = 28
name = 'Jonas'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

#nome2 = input("Informe o seu nome: ")

#operadores de comparação

saldo = 450
saque = 200
print(saldo == saque) or print(saldo != saque) or print(saldo > saque) or print(saldo >= saque)

#atribuição com adição, subtração, divisão...
saldo2 = 500
saldo2 += 200
print(saldo2)


saldo3 = 2000
#saque = float(input("Informe o valor do saque: "))
if saldo3 >= saque:
    print("Realizando saque!")
if saldo3 <= saque:
    print("Saldo insuficiente!")

# Repetições
#texto = input("Informe um texto: ")
#VOGAIS = "AEIOU"
#for letra in texto:
#    if letra.upper() in VOGAIS:
#        print(letra, end="")
#else:print()  

# usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado
#opcao = -1
#while opcao != 0:
    #opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
#    if opcao == 1:
#        print("Sacando...")
#    elif opcao == 2:
#        print("Exibindo o extrato...")
#    else:
#        print("Obrigado por usar nosso sistema bancário, até logo!")

#interpolar variáveis em strings
nome4 = "leticia"
idade = 25
profissao = "fisioterapeuta"
linguagem = "tupi guarani"
print(f"Olá, me chamo {nome4}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
#fatiamento
print (nome4[1])
print (nome4[:5])

#funções
def exibir_mensagem_2(nome5="levy"):
    print(f"Seja bem vindo {nome5}!")
      
exibir_mensagem_2()

saldo_atual = float(input("Escreva o saldo atual do colaborador: "))
valor_deposito = float(input("Escreva do valor do depósito: "))
valor_retirada = float(input("Escreva o valor de retirada: "))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
Saldo_final = saldo_atual + valor_deposito - valor_retirada

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print("O saldo final é: {:.2f}".format(Saldo_final))

valor =float(input())

if valor > 0: 
  saldo = valor
  print ("deposito realizado com sucesso!")
  print ("saldo novo: ".format(saldo))
elif valor==0:
  print ("tente novamente...")
else:
   print ("tente com valor maior que zero...")

   #função útil para o calculo do imposto (baseado em aliquotas)
def calcular_imposto(salario):
  aliquota=0.00
  if (salario >=0 and salario <=1100):
    aliquota = 0.05

  elif (salario>= 1110.01 and salario <=2500):
    aliquota =0.05
    
  else:
    aliquota = 0.15

  return aliquota * salario
#ler os valores de entrada:
valor_salario = float(input())
valor_beneficios=float(input())
#calcula o imposto através da função "calcular_imposto":
valor_imposto = calcular_imposto(valor_salario)
#calclula e imprime a saída (com 2 casas decimais)
saida = valor_salario - valor_imposto + valor_beneficios
print(f'{saida:.2f}')


ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativos in ativos:
  print(ativos)

# Entrada de dados
saldo_total = int(input("informe o saldo total de sua conta bancária: "))
valor_saque = int(input("informe o valor do saque: "))

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
Saldo_novo = saldo_total - valor_saque

if saldo_total >= valor_saque:
    print(f"saque realizado com sucesso! Novo saldo: {Saldo_novo}")

else:
    print(f"Saldo insuficiente. Saque não realizado!")


valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
for _ in range(periodo):
  valor_final *= (1 + taxa_juros)

print("Valor final do investimento: R$ {:.2f}".format(valor_final))

saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual = saldo_atual + valor_deposito - valor_retirada

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print("O saldo final é: {:.1f}".format(saldo_atual))