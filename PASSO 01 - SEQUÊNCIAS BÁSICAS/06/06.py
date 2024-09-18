# Exercicio 06
# Função : Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
# Autor : Diego Rosas
# Data : 18/09/2024
# Seção de Declarações

numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor de {numero} é {antecessor}')
print(f'O sucessor de {numero} é {sucessor}')