# Verificação de Palíndromo: Faça um programa que receba uma lista de palavras
# e verifique se cada palavra é um palíndromo. Um palíndromo é uma palavra que
# permanece a mesma quando lida de trás para frente. O programa deve imprimir 
# “Sim” para palíndromos e “Não” para não palíndromos. Utilize end=' ' 
# no comando print para que os resultados sejam exibidos na mesma linha, 
# separados por espaços.

palavras = list(map(str, input("Palavras: " ).split()))



for x in palavras:
    palavra_invertida = x[::-1]

    if(x == palavra_invertida):
        print("Sim", end=' ')
    
    else:
        print("Não", end=' ')