nicks_consultados = []

while len(nicks_consultados) < 3:       # Len é uma função que contabiliza quantos valores uma variável pode assumir
  print("Quantidade {}".format(len(nicks_consultados)))     # Format se refere à mostrar a quantidade (len) de itens nos nicks_consultados

  player = (input('Digite o nick desejado:'))

  if player == 'Phil':
    print('Player encrenqueiro,nível de habilidades:razoável.')

    if 'Phil' not in nicks_consultados:
      nicks_consultados.append('Phil')      # Adiciona à variavel nicks_consultados o valor entre parênteses

  elif player == 'Knuckles' :               # Elif é uma abreviação de else if (senão se)
    print('Ótimo player,muito cooperativo,nível de habilidades:alta!')

    if 'Knuckles' not in nicks_consultados:
      nicks_consultados.append('Knuckles')  # Adiciona à variavel nicks_consultados o valor entre parênteses
  elif player == 'Bubble':
    print('Considerado um dos melhores players no game,extremamente flexível e\n adaptável ao jogo de seu parceiro,nível de habilidades:altíssima!')

    if 'Bubble' not in nicks_consultados:
      nicks_consultados.append('Bubble')    # Adiciona à variavel nicks_consultados o valor entre parênteses

print("Terminou")


#Explicação

# Eu criei um vetor nicks_consultados, onde eu vou salvar quais nicks já foram digitados.

# while len(nicks_consultados) < 3:

# Nesse trecho eu pego a quantidade de itens da lista enquanto for menor que 3 (o usuário
# não digitou todos os nicks pelo menos uma vez eu repito o processo.

# Dentro dos ifs eu verifico se o nick não está na lista caso ele não estiver eu adiciono.
