# Exercicios

#1. Crie um programa que receba números positivos do usuário e continue pedindo até que um número negativo seja inserido. Ao final, imprima a soma de todos os números positivos inseridos.


soma = 0

while True:
    num = int(input("Digite um numero : "))
    if num < 0:
        break
    soma = soma + num

print(f"A soma dos numeros é {soma}")

# 2) Um usuário vai inserir notas de alunos. O programa deve parar quando o usuário digitar -1. No final, mostre a média aritmética das notas válidas.

soma = 0
cont = 0
nota = 0

while nota != -1:
    nota = float(input("Digite a nota : "))
    if nota != -1:
        soma = soma + nota
        cont = cont + 1
        media = soma / cont
print(f"Media : {media}")


# 3) Faça um programa que converta graus Celsius para Fahrenheit. O programa deve continuar convertendo enquanto o usuário não digitar um valor negativo para Celsius.
