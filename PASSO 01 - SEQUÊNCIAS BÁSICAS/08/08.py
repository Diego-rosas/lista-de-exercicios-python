# Exercicio 08
# Função : Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas. 
# Autor : Diego Rosas
# Data : 30/09/2024
# Seção de Declarações

distancia = float(input("Digite uma distância em metros: "))
distanciaKm = (distancia) / 1000
distanciaHm = (distancia) / 100
distanciaDam =(distancia) / 10
distanciaDm = (distancia) * 10
distanciaCm = (distancia) * 100
distanciaMm = (distancia) * 1000
print()
print(f"A distância de {distancia}m corresponde a: ")
print()
print(distanciaKm,"km")
print(distanciaHm,"Hm")
print(distanciaDam,"Dam")
print(distanciaDm,"Dm")
print(distanciaCm,"Cm")
print(distanciaMm,"Mm")