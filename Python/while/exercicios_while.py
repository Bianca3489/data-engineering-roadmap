# Exercicios

#1. Crie um programa que receba números positivos do usuário e continue pedindo até que um número negativo seja inserido. Ao final, imprima a soma de todos os números positivos inseridos.


# soma = 0

# while True:
#     num = int(input("Digite um numero : "))
#     if num < 0:
#         break
#     soma = soma + num

# print(f"A soma dos numeros é {soma}")

# 2) Um usuário vai inserir notas de alunos. O programa deve parar quando o usuário digitar -1. No final, mostre a média aritmética das notas válidas.

# soma = 0
# cont = 0
# nota = 0

# while nota != -1:
#     nota = float(input("Digite a nota : "))
#     if nota != -1:
#         soma = soma + nota
#         cont = cont + 1
#         media = soma / cont
# print(f"Media : {media}")


# 3) Faça um programa que converta graus Celsius para Fahrenheit. 
# O programa deve continuar convertendo enquanto o usuário não digitar um valor negativo para Celsius.

# celsius = 0
# while celsius >= 0:
#     celsius = float(input("Digite a temperatura em graus Celsius : "))
#     if celsius >= 0:
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"A temperatura em Fahrenheit é {fahrenheit}")
#     else:
#         break
# print("Programa encerrado!")



#  Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’  
# e conte os valores de M e F e imprima a quantide de cada um. Só saia do codigo quando alguem digitar um valor diferente de M ou F.

Feminino = 0
Masculino = 0

while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == "M":
        Masculino = Masculino + 1
    elif sexo == "F":
        Feminino = Feminino + 1
    else:
        break
print(f"Quantidade de Homens: {Masculino}")
print(f"Quantidade de Mulheres: {Feminino}")