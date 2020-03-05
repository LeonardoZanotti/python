# while = enquanto

contatos = []		# Cria a lista contatos


isFinished = False		# Sentinel
w = 0		# O motivo de eu ter usado uma variável (nesse caso w) para ser o contador de contatos da lista ao invés de simplesmente usar 'len(contatos)' é por que len(contatos) é uma variável fixa que vai receber um valor no começo da operação e foda-se, não fica atualizando a cada rodada pelo que eu percebi, bem, talvez haja uma explicação melhor para isso, mas foi mais fácil usar uma variável mesmo

print('Você está na sua lista de contatos')
while isFinished == False:		# Condição
	z = 1
	y = 0
	g = 1
	c = 0
	d = 0
	x = 0
	contatos = sorted(contatos)			# Deixa os contatos em ordem alfabética o tempo todo (se fosse colocado antes do while ele ia deixar a lista vazia em ordem alfabética sem ficar atualizando)
	
	print("Digite 'a' para adicionar um contato, 'r' para remover um contato ou 's' para sair ")
	i = str(input())
	print('')

# Outra opção para esta parte seria colocar: i = str(input("Digite 'a' para adicionar um contato, 'r' para remover um contato ou 's' para sair/n"), tendo o mesmo efeito do código usado
	
	if i == 'a':
		contato = str(input('Digite o nome do contato que quer adicionar: '))
		
		while c < w:
			if contato == contatos[c]:
				g = 0
				print(contato,'já está nos seus contatos')
			c += 1
			
		if g == 1:	
			contatos.append(contato)
			print(contato,'foi adicionado(a) aos contatos')
			w += 1
		print('')
		
		
	elif i == 'r':
		print('Lista de contatos')
		while x < w:
			print(contatos[x])
			x += 1
			
		contato = str(input('Digite o nome do contato que quer remover: '))
		
		while y < w:
			if contato == contatos[y]:
				contatos.remove(contato)
				z = 0
				print(contato,'foi removido(a) dos contatos')
				w += -1
			y += 1
			
		if z == 1:	
			print('Contato não encontrado')
		print('')
		
		
	elif i == 's':
		print('Saindo...')
		isFinished = True
		
		
	else:
		print('Lista de contatos')
		while d < w:
			print(contatos[d])
			d += 1
		print('')