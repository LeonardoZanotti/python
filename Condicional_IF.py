# IF = Se

idade = None

# print("Digita a sua idade ae meu:")	# Outra opção de input
# idade = int(input())

idade = int(input("Digita a tua idade ae meu: "))		# o int serve pra deixar claro que a variável é do tipo inteiro, se não tivesse int ali seria necessário usar 'idade = int(idade)' posteriormente
print('bls man sua idade é',idade,'kkk caraio')

if idade <= 12: 
	print('CARALHO MENOR TU É MÓ KID, SOME DAQ MEU, SOME DAQ')
elif idade <= 18:		# Não é necessário indicar 'idade > 12' pois elif é como um else que só ocorrerá caso o primeiro if não funcione
	print('kkk vc é jovem né kkk masa')
else:
	print('caraio pora tu é veiao kk vai more')
	
print('')
print('Bora vê uns booleano ae meu parcero kk')
print('Quem digitou a idade é gay:',idade<0)		# True independente do que acontecer
print('idade menor que 12 anos:',idade<12)
print('idade igual 12 anos:',idade==12)
print('idade maior que 12 anos e menor que 18 anos:',12<idade<18)
print('idade igual a 18 anos:',idade==18)
print('idade maior que 18 anos e menor que 30 anos:',18<idade<30)
print('idade igual a 30 anos:',idade==30)
print('idade maior que 30 anos e menor que 45 anos:',30<idade<45)
print('idade igual a 45 anos:',idade==45)
print('idade maior que 45 anos:',idade>45)
print('Quem digitou a idade é corno:',idade>=0)