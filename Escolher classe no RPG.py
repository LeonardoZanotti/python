#Setando todos as classes possiveis para escolher, se quiser é só adicionar mais classes
CLASS = {
    'Phil': 'Player encrenqueiro, nível de habilidades: razoável.',
    'Knuckles': 'Ótimo player, muito cooperativo, nível de habilidades: alta!',
    'Bubble': 'Considerado um dos melhores players no game, extremamente flexível e\n adaptável ao jogo de seu parceiro, nível de habilidades: altíssima!',
    'Woss': 'Pica das galáxias. Com certeza o melhor! Boa escolha, nível de habilidades: mais que 8000!'
}

#Se não escolher nenhuma delas, mostra-se essa mansagem
DEFAULT = 'Huum, não sei o que dizer sobre esse player :('

#Enquanto for verdade, enquanto nada parar o processo
while True:
    print("Qual classe gostaria de utilizar?")
    print("Que tal essas opções:", list(CLASS.keys()), '?')     # Lista todas as Classes inseridas no CLASS

    classe = input("Classe: ")  #Input --> algo inserido pelo usuário

    print(CLASS.get(classe, DEFAULT))   # Ele mostra o texto conforme sua classe, primeiro analisa no CLASS, se não achar a classe ele mostra o DEFAULT

    confirm = input('Gostaria de manter essa classe? [s/n] ')

    if confirm in ['S', 's', '']:
        break       # Para o processo
    else:           # Se não
        print()         

print('Ok, sua classe será {}'.format(classe))      # .format é um modo de representar uma variável sendo que a variável já é convertida para um type adequado

# Não dá pra ver aqui, mas o fato desse ultimo print esta na mesma "coluna" do while o tira do comando, então o while true pega até o 'print()', daí ele
# repete denovo atpe ser false, sair do while e ir pra esse print
