# Número de inicio; Número Final, Passo
# for (Variável) in range((NúmeroInicial), (NúmeroFinal), (Passo))
for i in range(100):	#Caso não seja estipulado um ponto inicial a função irá contabilizar como sendo 0
	print(i)			
	
# A função for funciona de modo que quando a variável (nesse caso 'i') atinge o número final, a função para ao invés de rodar mais uma vez, sendo que irá gerar então (nesse caso) números até atingir um número antes do número final, nesse caso, até o 99
print('')
for x in range(5, 100):	# A Contagem começa no número 5
	print(x)			# Do mesmo modo, a função para em um algarismo antes do último do range (nesse caso ainda é o 99)
	
print('')
print('Números Pares de um até 100')
for a in range(0, 101, 2):
	print(a)
print('')
print('Números Ímpares de um até 100')
for b in range(1, 100, 2):
	print(b)

print('')
print('Números primos de 0 até 100')
for c in range(2, 101):
	y = 0
	for x in range(1, c+1):
		if (c % x) == 0:
			y += 1
	if y == 2:
		print(c)
	