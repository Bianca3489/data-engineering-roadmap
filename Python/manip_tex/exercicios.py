# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

# nome = input('Digite seu nome completo: ')
# print(nome.upper())
# print(nome.lower())
# print(len(nome.replace(' ', '')))
# print(len(nome.split()[0]))

# Exercício Python 23: 
# Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.

# numero = int(input('Digite um número de 0 a 9999: '))

# if numero > 9999:
#     print('Número inválido')
# else:
#     print('Unidade: ', numero // 1 % 10)
#     print('Dezena: ', numero // 10 % 10)
#     print('Centena: ', numero // 100 % 10)
#     print('Milhar: ', numero // 1000 % 10)

# Exercício Python 24: Crie um programa que leia o nome 
# de uma cidade diga se ela começa ou não com o nome “SANTO”.

# cidade = input('Digite o nome nome da cidade: ').lower()
# if cidade.startswith('santo'):
#     print('Essa cidade começa com santo')
# else:
#     print('Essa cidade não começa com santo')

# Exercício Python 25: Crie um programa que leia o nome 
# e uma pessoa e diga se ela tem “SILVA” no nome.

# nome = input('Digite seu nome completo: ').lower()
# if 'silva' in nome:
#     print('Essa pessoa tem SILVA no nome')
# else:
#     print('Essa pessoa não tem SILVA no nome')

# Exercício Python 26: Faça um programa que leia uma frase pelo teclado 
# e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# fraset = input('Digite uma frase: ').lower().strip()
# print(f'A letra A aparece {fraset.count('a')} vezes na frase')
# print(f'A letra A aparece pela primeira vez na posição {fraset.find('a')+1}')
# print(f'A letra A aparece pela última vez na posição {fraset.rfind('a')+1}')

# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente. 
#  Exemplo: Entrada: Maria Oliveira Silva, Saída: Maria Silva

# import exercicios
# nome = input('Digite seu nome completo: ').strip()
# print('Primeiro nome: ', nome.split()[0])
# print('Último nome: ', nome.split()[-1])