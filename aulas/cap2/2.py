# Escreva um programa que solicite ao usuário que insira uma palavra ou frase. Em seguida,
#  o programa deve imprimir o comprimento da string, a primeira letra da string, a última letra da string e a string invertida.


frase = input("escreva: ")

comprimento = len(frase)

print(f"comprimento: {comprimento}\nprimeira letra: {frase[0]}\nultima letra: {frase[-1]}\ninvertida: {frase[::-1]}")