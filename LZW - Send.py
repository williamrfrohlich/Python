#------------------------------------------------------------------
#		Author: William da Rosa Frohlich
#
#		Company: Feevale University
#
#		Project: Lempel Encoding
#
#		Date: 05.23.2019
#
#------------------------------------------------------------------

import socket			# Importar bibliotecas para socket

# AF_INIT == Protocolo de endereço de IP
# SOCK_DGRAM == Protocolo de transferencia UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)				

address = ('127.0.0.1', 5000)			# Endereco de Conexao

while True:			# Loop principal
	
	msg = input()			# Leitura da mensagem que sera enviada

	c = "";	p = "";	p_auxi = ""; SC = ""			# Inicializacao das variaveis com valor nulo
	
	dicio = ("a","b","c",)			# Inicializacao do dicionario

	for i in range(len(msg)):			# Loop para passagem de caractere por caractere da mensagem
		print (dicio)			# Imprime o dicionario na tela
		c=msg[i]			# Variavel c recebe caractere i da mensagem recebida
		conc = p + c				# Concatena variaveis p + c
		
		for j in range(len(dicio)):			# Loop para verificar se a variavel "conc" faz parte do dicionario...
			
			if conc == dicio[j]:			# Teste condicional para verificar se "conc" esta presente no dicionario
				conc_dicio = 1				# Variavel auxiliar para caso "conc" esteja presente no dicionario
		
		if conc_dicio == 1:			# Se variavel auxiliar for 1...

			p = conc			# p recebe a variavel conc
			conc_dicio = 0			# Variavel auxiliar recebe valor 0

		else:			# Se variavel auxiliar for 0...

			for j in range(len(dicio)):			# Loop para verificar se "p" faz parte do dicionario...

				if p == dicio[j]:			# Teste condicional para verificar se "p" esta presente no dicionario

					p_auxi = str(j)			# "p_auxi" recebe a posicao equivalente de "p" no dicionario

			SC = SC + p_auxi 			# "p_auxi" atribui seu valor ao final de SC
			dicio+=(conc,)			# A variavel "conc" e adicionado ao dicionario
			p = c			# "p" recebe o valor atual de "c"
			p_auxi = ""			# "p_auxi" recebe valor nulo

	
	for j in range(len(dicio)):			# Loop para verificar se "c" este presente no dicionario
			
		if c == dicio[j]:			# Condicional para verificar se "c" pertence ao dicionario
			num_SC = str(j)			# Variavel auxiliar "num_SC" recebe a posicao da ultima letra da string
	
	SC = SC + num_SC			# Posicao da ultima variavel da string atribui na sequencia codificada
	print("Mensagem decodificada = ", msg)			# Imprime na tela a mensagem digitada
	print("Mensagem codificada = ", SC)			# Imprime na tela a mensagem codificada
	sock.sendto(SC.encode('UTF-8'),address)							# Envio da mensagem lida ao servidor UDP
