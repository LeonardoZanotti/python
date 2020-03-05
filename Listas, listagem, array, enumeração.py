# listas

"""													# Comentário de múltiplas linhas
Listas, arrays, vetores
são
conjuntos de dados
"""													# Comentário de múltiplas linhas

nomes = ['Ana', 'Paula', 'Roberta']		# Lista nomes com as strings

print('')
print("Quantidade de itens na lista nomes:",len(nomes))					# Retorna quantos itens a lista nomes possui (função len) 
print('')
print("Itens da lista nomes:")
for nome in nomes:					# nome é uma variável temporária que varia a cada item da lista nomes
	print (nome)					# A cada variação de nome, a variável é exibida na tela, sendo então uma listagem dos nomes da lista
print('')							# Esse, como está logo abaixo da função na mesma coluna é exibido uma única vez após a função ser executada
print("Fim da listagem")	
	#print('')						# Esse print, por estar na mesma linha do corpo da função for seria repetido após cada nome (se estivesse na sequência)
print('')					
	
print (nomes)						# Exibe a lista nomes por completo	


# Adicionando nomes na lista indiretamente
nomes.append("Thiago")		# Adiciona o nome "Thiago" à lista
nomes.append("Rafael")		# Adiciona o nome "Rafael" à lista
print('')
print('')
print("Quantidade de itens na lista nomes:",len(nomes))	
print(nomes)
for nome in nomes:
	print (nome)
print('')
nomes.remove("Ana")			# Remove o nome "Ana" da lista
print(nomes)
for nome in nomes:
	print(nome)
print("Quantidade de itens na lista nomes:",len(nomes))	

print('')
nomes.append("Maria")
nomes.append("Ana")
nomes.append("José")
nomes.append("Zanotti")
nomes.append("Bianca")
nomes.append("Leonardo")
#built-in
#ordenar em sort
# Com o 'sorted' a listagem fica ordenada em ordem alfabética
for nome in sorted(nomes):	
	print(nome)
	
print('')
print('')
#built-in
#ordenar em sort
#ordenando a lista com o sorted de outro modo
nomes = sorted(nomes)			# Com isso, é como se a lista já estivesse organizada antes de iniciar a listagem
for nome in nomes:				# A listagem é literalmente um nome após o outro, primeiro nome, segundo nome, sem tentar organizar nada, entretanto a listagem vem em ordem alfabética pois a lista está em ordem alfabética
	print(nome)
	
print('')
print('Listando manualmente')
print(nomes[0])			# Nomes[x] se refere ao nome (item) na posição x da lista
print(nomes[1])			# Os nomes estão em ordem alfabética pois foi definido isso anteriormente 
print(nomes[2])			# nomes[[indice]; Com isso têm-se que um elemento em si (item da lista) é matemáticamente igual ao índice somado a uma unidade 
print(nomes[3])			# índice + 1 = elemento --> índice 2 é o elemento 3 da lista
print(nomes[4])	
print(nomes[5])	
print('')
print('Fazendo isso automáticamente')	
for	i in range(0, len(nomes)):		# Começa em 0 pois nas listas o primeiro elemento é na verdade o elemento número zero 
	print(nomes[i])
print('')

print ('Enumerando cada elemento da lista')
for i in range(0, len(nomes)):
	print('Índice',i,'é igual ao elemento',nomes[i])
	
print('')	
nome = "Ana"		# Para Soletrar outro nome é só mudar aqui
print ('Enumerando cada letra de um nome')
for i in range(0, len(nome)):
	print('Índice',i,' é igual ao elemento',nome[i])

print('')
print('Soletrando todos os nomes')
for x in range(0, len(nomes)):
	nome = nomes[x]
	for y in range(0, len(nome)):
		print(nome[y])
	print('')	

	
print('')
print('Contando as letras dos nomes')
for x in range(0, len(nomes)):
	nome = nomes[x]
	for y in range(0, len(nome)):
		print('Índice',y,' é igual a letra',nome[y])
	print('')	
	
print("")
print('Enumerando os nomes')
for i, nome in enumerate(nomes):
	print(i,'=',nome)