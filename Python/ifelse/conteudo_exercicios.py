# Condições aninhadas

# Conceito de condições aninhadas

# Estrutura de decisão onde uma estrutura de decisão está dentro de outra.
# A indentação é fundamental para que o código funcione.
# A lógica é que se a primeira condição for verdadeira, a segunda condição será verificada.

# Exemplo:

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
    if idade >= 60:
        print('Você é idoso.')
    else:
        print('Você é adulto.')
else:
    print('Você é menor de idade.')


# Exemplo 2:

num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O número é par.')
    if num % 3 == 0:
        print('O número é divisível por 3.')
    else:
        print('O número não é divisível por 3.')
else:
    print('O número é ímpar.')


# Exemplo 3 aninhada:

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
    if numero % 2 == 0:
        print("E também é par.")
    else:
        print("E também é ímpar.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")




# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint
from time import sleep

computador = randint(0,5)
print('='*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar!')
print('='*30)
jogador = int(input('Em que numero pensei? '))
print('PROCESSANDO')
sleep(3)
if jogador == computador:
    print('Parabens, voce acertou!')
else:
    print(f'Ganhei! Eu pensei no {computador}')

# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = float(input('Qual é a velocidade atual do carro? '))
valor_multa = (velocidade_carro - 80) * 7

if velocidade_carro > 80:
    print('Você foi multado!')
    print(f'O valor da sua multa é de R$ {valor_multa:.2f}')
else:
    print('Você está dentro do limite de velocidade! Tenha um bom dia e dirija com segurança.')

# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = float(input('Qual é a distância da sua viagem em Km? '))

if distancia <= 200:
    preco_passagem = distancia * 0.50
    print(f'O valor da sua passagem é de R$ {preco_passagem:.2f}')
else:
    preco_passagem = distancia * 0.45
    print(f'Sua viagem é longa e o valor da sua passagem é de R$ {preco_passagem:.2f}')

# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('As retas podem formar um triângulo.')
    if a == b == c:
        print('Os comprimentos formam um triângulo equilátero.')
    elif a == b or a == c or b == c:
        print('Os comprimentos formam um triângulo isósceles.')
    else:
        print('Os comprimentos formam um triângulo escaleno.')
else:
    print('As retas não podem formar um triângulo.')


