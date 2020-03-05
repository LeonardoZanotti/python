# while = enquanto

maior = 100			# Maior número
contador = 0		# Menor número que irá crescer até atingir o maior número e gerará o loop
while contador < maior:		# enquanto o contador for menor que o maior (100) faça o seguinte: 
	contador += 1			# Adicione 1 ao continue
	print(contador)			# Mostre o contador
	
# A função while, do jeito escrito acima, vai até o número da maior variável (maior(100)), sendo então uma contagem de 0 até 100; Diferentemente da função for, que iria até 99
# Dá pra fazer um loop do tipo, enquanto tal tecla é pressionada, ou enquanto tal tecla não for pressionada, só que isso é mt elevado

print('')
contador = 0
while contador < maior:		# enquanto o contador for menor que o maior (100) faça o seguinte: 
	print(contador)			# Mostre o contador
	contador += 1			# Adicione 1 ao continue
	
# Como pode-se ver, a ordem do print e do 'adicionar 1' importam para o funcionamento da função, sendo que do primeiro modo ela vai até 100 e no segundo modo ela vai até 99; Entretanto, na primeira função a contagem começa em 1 e na segunda em 0