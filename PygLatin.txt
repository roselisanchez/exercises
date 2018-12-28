#Pig Latin em Python :D
#Pig Latin é um jogo onde a primeira letra da palavra é colocada no final da mesma, acrescentando o sufixo "ay"
#exemplo Python -> ythonpay

print ("Bem-vindo ao tradutor Pig Latin!")

pyg = "ay"

original = input("Digite uma palavra: ")


if len(original) > 0 and original.isalpha():	#verifica se a palavra foi digitada e é formada somente por letras
	word = original.lower()			#deixa a palavra em minúsculas
	first = word[0]				#armazena a primeira letra da palavra
	new_word = word + first + pyg		#concatena strings para formar a palavra em Pig Latin
	new_word = new_word[1:len(new_word)]	#fatia a string para não mostrar a primeira letra					

	print("Tradução: ", new_word)
else:
	print("Vazio ou uso de caracteres que não são letras")









