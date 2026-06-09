
# 1 ) imprima cálculo do KPI para o usuário = 1000 + salario * bonus
# Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus


constante_valor = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
bonus = float(input("Digite o valor do seu bonus: "))
calc_kpi = constante_valor + salario * bonus
print(f"Olá {nome}, seu bonus é: R$ {calc_kpi}")
