# Faça um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# O IMC é calculado dividindo-se o peso da pessoa pela sua altura ao quadrado. 
# O IMC é uma medida da relação entre o peso e a altura de uma pessoa. O programa 
# deve imprimir o IMC da pessoa, classificando-o de acordo com a tabela abaixo:

peso = float(input("peso: "))
altura = float(input("altura: "))

imc = peso/(altura**2)

if imc <= 18.5:
    print("Abaixo do peso")

elif imc <= 24.9:
    print("Saudável")

elif imc <= 29.9:
    print("Sobrepeso")

elif imc <= 34.9:
    print("Obesidade grau I")

elif imc <= 39.9:
    print("Obesidade grau II")

else:
    print("Obesidade grau III")

