# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


# from math import trunc

# num = float(input('Digite um numero: '))
# print(trunc(num))

# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

# from math import hypot

# co = float(input("Digite o cateto_oposto: "))
# ca = float(input("Digite o cateto_adjacente: "))
# # hipotenusa = (ca ** 2 + co ** 2) ** (0.5) 
# hi  = hypot(co, ca)
# print(f'A hipotenusa é : {hi:.2f}')


# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# import random
# alunos = ['Derick', 'Bianca', 'Fabio', 'Aleixa', 'Marcelo']
# escolhido = random.choice(alunos)
# print(f'{escolhido} vai apagar o quadro hoje')

# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# import random

# a1 = input('Digite o primeiro aluno: ')
# a2 = input('Digite o segundo aluno: ')
# a3 = input('Digite o terceiro aluno: ')
# a4 = input('Digite o quarto aluno: ')
# lista = [a1, a2, a3, a4]
# random.shuffle(lista)
# print(f'A ordem sorteada')
# print(lista)

# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# pyrefly: ignore [missing-import]
# import pygame

# pygame.init()
# pygame.mixer.music.load('musica.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()
