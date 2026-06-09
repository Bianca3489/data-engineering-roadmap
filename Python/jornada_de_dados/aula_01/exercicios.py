# # Crie programa que o usuário digita o seu nome e retorna o número de caracteres

# nome = input("Digite seu nome: ")
# print (f"Olá {nome}, seu nome tem {len(nome)} letras.")

#  Crie programa que o usuário digita o número e retorna se é par ou ímparpar

# num = int(input("Digite um número: "))

# if num % 2 == 0:
#     print(f"{num} é par")
# else:
#     print(f"{num} é ímpar")
    
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# print(f"A soma de {num1} e {num2} é {num1 + num2}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num = int(input("Digite um número: "))

# print(f"O resto da divisão de {num} por 5 é {num % 5}")
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# try:
#     num1 = int(input("Digite um numero inteiro:"))
#     num2 = int(input("Digite um  outro numero inteiro:"))
#     resultado_divisao = num1 // num2
#     print(f"A divisao inteir dos dois numeros é : {resultado_divisao}")
# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida")
# except ValueError:
#     print("Erro: Você deve digitar um número inteiro.")

try:
    resultado = len(10)
except TypeError as e:
    print(f"Erro de tipagem: {e}")

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# print(f"A divisão inteira de {num1} por {num2} é {num1 // num2}")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num  = int(input("Digite um numero: "))
# print(f"O quadrado de {num} é {num ** 2}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# num1 = float(input("Digite um numero: "))
# num2 = float(input("Digite outro numero: "))
# print(f"A soma de {num1} e {num2} é {num1 + num2}")   
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.   

# num1 = float(input("Digite um numero: "))
# num2 = float(input("Digite outro numero: "))
# print(f"A média de {num1} e {num2} é {(num1 + num2) / 2}")   

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
# print(f"A potencia de {base} elevada a {expoente} é {base ** expoente}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string = input("Digite uma string: ")
# print(f"String em maiucusla: {string.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# string = input("Digite uma string: ")
# print(f"String em maiucusla: {string.lower()}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# string = input("Digite uma string: ")
# print(f"String em maiucusla: {string.strip()}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato dd/mm/aaaa: ")
# data_formatada = data.split("/")
# print(f"Dia : {data_formatada[0]}")
# print(f"Mes : {data_formatada[1]}")
# print(f"Ano : {data_formatada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string1 = input("Digite a primeira palavra: ")
# string2 = input("Digite a segunda palavra: ")
# print(f"As duas palavras juntas são: {string1 + " " + string2}")
# #### Booleanos (`bool`)

# 16: Escreva um programa que pergunte a 
# quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
# km = float(input("Digite a quantidade de Km percorridos pelo carro: "))
# calculo_dias = 60 * dias
# calculo_km = 0.15 * km
# print(f"O preço a pagar pelo carro é R$ {calculo_dias + calculo_km}")

# 17. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.


# 18. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 19. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 20. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 21. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 22: Conversor de Temperatura
# 23: Verificador de Palíndromo
# 24: Calculadora Simples
# 25: Classificador de Números
# 26: Conversão de Tipo com Validação

    