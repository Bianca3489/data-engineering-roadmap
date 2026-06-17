## if else aninhado

# Conceito

#if 1:
    #if 2:
        #if 3:
            #if 4:
                #if 5:
                    #if 6:
                        #if 7:
                            #if 8:
                                #if 9:
                                    #if 10:
                                       

# O conceito de if aninhado é que você pode ter um if dentro de outro if.
# Ou seja, se a primeira condição for verdadeira, a segunda condição será verificada.
# Se a segunda condição for verdadeira, a terceira condição será verificada.
# E assim por diante.
# A indentação é fundamental para que o código funcione.
# A indentação é feita com 4 espaços.

# Exemplo 1

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você é menor de idade')  
    if idade < 13:
        print('Você é criança')  
    else:
        print('Você é adolescente')
else:
    print('Você é maior de idade')

# Exemplo 2

salario = float(input('Digite seu salário: '))

if salario <= 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f'Seu novo salário é de R$ {novo_salario:.2f}')   
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f'Seu novo salário é de R$ {novo_salario:.2f}')


# Exemplo 3

numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print('O numero é par')
    if numero % 3 == 0:
        print('O numero é divisivel por 3')
    else:
        print('O numero não é divisivel por 3')
else:
    print('O numero é impar')
    if numero % 3 == 0:
        print('O numero é divisivel por 3')
    else:
        print('O numero não é divisivel por 3')

# Exercicios
# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite quantos anos você vai pagar: '))

prestacao = valor_casa / (anos * 12)

if prestacao <= salario * 30 / 100:
    print(f'Empréstimo aprovado, prestação de R$ {prestacao:.2f}')
else:
    print(f'Empréstimo negado, prestação de R$ {prestacao:.2f}')

