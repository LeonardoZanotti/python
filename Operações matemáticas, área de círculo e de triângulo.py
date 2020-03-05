pi = 3.1415926535
print(pi)
print(1/3)
print(1/3.0)

x = 5
y =9
print("Multiplicação:")
print(x*y, x/y)
print(x+y, x-y)

#Obtendo informações sobre um círculo
raio = 9
print("")
print("Círculo")
print("Raio =", raio)
print("")
area = pi*raio*raio
comprimento = 2*pi*raio
print("Área: ", area)
print("")
print("Comprimento: ", comprimento)

# Se quiser pode escrever assim também:
# print("Comprimento") ou print("Área")
# print(comprimento) ou print(area)
# Desse modo o valor aparece em baixo do texto e não do lado como acontece em print("Comprimento:", comprimento)


#Obtendo informações sobre um triângulo
h = 3			# Altura
base = 4.5
area = base * h/2
print("Ent man, teu triângulo tem base de", base,"metros e altura de", h,"metros, por isso eu acho que a área dele é de", area,"metros quadrados")