#Fatiamento de strings

frase = "Voce é linda mais que demais, voce é linda sim, onda do mar do amor que bateu em mim"
email = 'bia.rscr@hotmail.com'

email2 = input('Digite seu email: ')
if '@'in email2:
    print('Email válido')
else:
    print('Por favor digite um email válido que tenha @')

print(frase[0])
print(frase[7:11])
print(frase[0:13:2])
print(frase[:5])
print(frase[13:])
print(frase[9::3])
print(frase[:-1])

# Funcoes

print(len(frase))
print(frase.count('a'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.replace('a', '@'))
print(email.split('@'))
print(frase.find('linda'))
print(email.find('@'))
print(frase.find('a', 2))
print(frase.strip()) #remove espaços no inicio e no fim
print(frase.rstrip()) #remove espaços no final
print(frase.lstrip()) #remove espaços no inicio
print(frase.startswith('Voce'))
print(frase.endswith('mim'))

# Funcionalidades de divisao

frasenova = frase.split(',')
print(frasenova)
frasej = ' '.join(frase)
print(frasej)

