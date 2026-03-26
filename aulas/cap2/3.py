# Escreva um programa que compare duas strings fornecidas pelo usuário, considerando 
# valores booleanos "True" ou "False". O programa deve ignorar diferenças de capitalização 
# (maiúsculas e minúsculas) e imprimir na tela se as strings são iguais ou diferentes.

entrada1 = input("entrada 1:")
entrada2 = input("entrada 2:")

entrada1 = entrada1.upper()
entrada2 = entrada2.upper()

if entrada1 == entrada2:
    print("são iguais")

else:
    print("são  diferentes")
