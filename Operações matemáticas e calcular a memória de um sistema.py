print('')
print (2 + 2)				# 4
print (2 - 2)				# 0
print (2 * 2)				# 4
print (2 / 2)				# 1.0
print (2 % 2)				# 0				# Resto da divisão de 2 por 2
print (abs(-2))				# 2				# Valor absoluto --> é o mesmo que |-2|
print (pow(2, 32))			# 4294967296	# 2^32 (2**32) --> Sistema 32-bits (x86) suporta essa quantidade de bytes (Sistema 64-bits suporta 2^64 bytes)		
print (2**32)				# 4294967296	# 2^32 (2**32) --> Sistema 32-bits (x86) suporta essa quantidade de bytes (Sistema 64-bits suporta 2^64 bytes)	
print('')
print ("2" + "2")			# 22
# print ("2" - "2")			# Erro
# print ("2" * "2")			# Erro			# abs() e pow() é função built-in
# print ("2" / "2")			# Erro
# print ("2" % "2")			# Erro
# print (abs("-2"))			# Erro
# print (pow("2", "32"))	# Erro	
# print ("2"**"32")			# Erro
print('')
print ("2 + 2")				# 2 + 2
print ("2 - 2")				# 2 - 2
print ("2 * 2")				# 2 * 2
print ("2 / 2")				# 2 / 2
print ("2 % 2")				# 2 % 2
print ("abs(-2)")			# abs(-2)
print ("pow(2, 32)")		# pow(2, 32)		
print ("2**32")				# 2**32






# Quanta memória os sistemas 32 e 64 bits suportam
a = int(32)												# Se quiser saber de outro sistema com outra taxa de bits é só modificar o 32
b = int(64)												# Se quiser saber de outro sistema com outra taxa de bits é só modificar o 64
mema = int(pow(2, a))		
memb = int(pow(2, b))	
mema1024 = float(mema/1024)
memb1024 = float(memb/1024)

print('')
print('')
print("Memória", a,"bits")
print("B: %0.0f" %mema)									# Bytes
print("KB: %0.0f" %mema1024)							# Kilobytes
print("MB:",mema / 1024 / 1024)							# Megabytes
print("GB:",mema / 1024 / 1024 / 1024)					# Gigabytes
print('')
print("Memória", b,"bits")
print("B: %0.0f" %memb)
print("KB: %0.0f" %memb1024)
print("MB:",memb / 1024 / 1024)
print("GB:",memb / 1024 / 1024 / 1024)