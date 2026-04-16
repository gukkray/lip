# Classificação Etária: Desenvolva um programa que recebe várias idades de usuários na entrada, 
# todas separadas por espaços. Para cada idade, o programa deve imprimir a categoria correspondente 
# de acordo com a seguinte escala:

idades = list(map(int, input("Digite as idades separada por espaços: ").split()))

for x in idades:
    if (x < 13 ):
        print("Menor de idade")
    
    elif (13 <= x < 18 ):
        print("Adolescente")

    elif (18 <= x < 60 ):
        print("Maior de idade")

    else:
        print("Idoso")



# for x in idades:
#     if (x < 13 ):
#         print("Menor de idade")
    
#     elif (x < 18 ):
#         print("Adolescente")

#     elif (x < 60 ):
#         print("Maior de idade")

#     elif (x >= 60 ):
#         print("Idoso")