# Crie um programa que solicite ao usuário a inserção de cinco frutas diferentes. 
# Antes da leitura dos dados, crie uma lista vazia chamada frutas. Em seguida, armazene 
# as frutas fornecidas pelo usuário nessa lista e, ao final, imprima a lista completa na tela.

frutas = []

for x in range(5):
    entrada = input("digite uma fruta: ")
    frutas.append(entrada)

print(f"{', '.join(frutas)}")