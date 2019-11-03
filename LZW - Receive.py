#------------------------------------------------------------------
#		Author: William da Rosa Frohlich
#
#		Company: Feevale University
#
#		Project: Lempel Decoding
#
#		Date: 05.23.2019
#
#------------------------------------------------------------------

import socket			# Importar bibliotecas para socket

# AF_INIT == Protocolo de endereco de IP
# SOCK_DGRAM == Protocolo de transferencia UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

address =('',5000)			# IP e Porta do servidor
sock.bind(address)			# Abertura do socket de conexao

while True:			# Loop para aguardar mensagens
	
	SC= sock.recv(1024)			# Aceita a conexao e armazena a mensagem recebida
	msg=SC.decode('UTF-8')			# Decodifica a mensagem recebida
	
	stri_cW = ""; cW = ""; pW = ""; p = ""; c = "";	SS = ""; conc_dicio = 0			# Inicializacao das variavel com valor nulo
	
	dicio = ("a","b","c",)			# Inicializacao do dicionario

	for i in range(len(msg)):			# Loop para passagem de caractere por caractere da mensagem
		print (dicio)			# Imprime o dicionario na tela
		cW=int(msg[i])			# "cW" recebe caractere recebido
		pW=cW			# "pW" recebe "cW"
		
		if (i+1)<len(msg):			# Se o valor de "i+1" for menor que o tamanho da mensagem recebida...
		
			cW_auxi=int(msg[i+1])			# Varivael "cW_auxi" recebe o proximo caractere
				
		if  cW_auxi < len(dicio):			# Se "cW_auxi" for menor que o tamanho do dicionario...
			
			conc_dicio = 1			# Variavel auxiliar "conc_dicio" recebe 1
			stri_cW = dicio[cW]			# "stri_cW" recebe valor da posicao equivalente do dicionario
		
		if conc_dicio == 1:			# Se "conc_dicio" for 1...
			
			SS = SS + stri_cW			# "SS" concatena "stri_cW"
			p = dicio[pW]			# "p" recebe caractere do dicionario equivalente da posicao "pW"
			c = dicio[cW_auxi]			# "c" recebe caractere do dicionario equivalente a posicao "cW_auxi"
			conc = p + c[0:1]			# "conc" recebe a concatencao de "p" e o primeiro caractere de "c"
			dicio+=(conc,)			# Adiciona "conc" ao dicionario
			conc_dicio = 0			# Variavel auxiliar "conc_dicio" recebe valor nulo
		
		else:			# Se "conc_dicio" for 0...

			p = dicio[pW]			# "p" recebe caractere do dicionario equivalente da posicao "pW"
			c = dicio[cW]			# "c" recebe caractere do dicionario equivalente a posicao "cW_auxi"
			conc = p + c[0:1]			# "conc" recebe a concatencao de "p" e o primeiro caractere de "c"
			dicio+=(conc,)			# Adiciona "conc" ao dicionario
			stri_cW = dicio[cW]			# "stri_cW" recebe caractere do dicionario equivalente a posicao "cW"
			SS = SS + stri_cW			# Adiciona "stric_cW" ao final da sequencia de saida 

	
	print("Mensagem codificada = ", msg)			# Imprime a mensagem recebida
	print ("Mensagem decodificada = ", SS)			# Imprime na tela a mensagem recebida decodificada
