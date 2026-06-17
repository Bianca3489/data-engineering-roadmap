# Faça um programa que digite um numero e mostre a sua tabuada de 1 a 10

n = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")


# Faça um programa que some todos os números de 1 até 100

n = 1

for i in range(1, 11):
    n += i
    print(n)

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range(1, 51):
    print(i)

#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. 

soma_idade = 0
for i in range(4):
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    soma_idade += idade 

    if i == 0:
        mais_velho = nome
        idade_velho = idade
        if sexo == "F" and idade < 20:
            mulheres_20 = 1
        else:
            mulheres_20 = 0
    else:
        if idade > idade_velho:
            mais_velho = nome
            idade_velho = idade
        if sexo == "F" and idade < 20:
            mulheres_20 += 1

print("Média de idade: ", soma_idade / 4)
print("Homem mais velho: ", mais_velho)
print("Mulheres com menos de 20 anos: ", mulheres_20)

