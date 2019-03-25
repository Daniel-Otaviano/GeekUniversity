"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo

Em Python, string é tudo que estiver entre:
- Aspas simples -> 'Daniel'
- Aspas duplas -> "Daniel"
- Aspas simples triplas -> '''Daniel'''
"""
'''
- Aspas duplas triplas -> """Daniel"""
'''

# Entrada de dados
#print("Qual o seu nome? ") #Apenas printa na tela
#nome = input() #input -> Entrada

nome = input('Qual seu nome? ')
#Exemplo de print 'antigo' versão 2.x
#print("Seja bem-vindo(a) %s" % nome) #Usando o %s

#Exemplo de print 'moderno' versão 3.x
#print("Seja bem-vindo(a) {0}".format(nome)) #Usando o .format()

#Exemplo de print 'mais atual' versao 3.7
print(f'Seja bem-vindo {nome}') #o f deve estar junto com a string -> f'exemplo{variavel}'

#print("Qual a sua idade? ")
#idade = input()
idade = input('Qual a sua idade? ')

#Processamento

#Saída de dados
#Exemplo de print 'antigo' versão 2.x
#print("%s tem %s anos" % (nome, idade)) #Para inserir mais variáveis é necessário colocar -> % (variavel1,variavel2)

#versao de print 'moderno' versao 3.x
#print("{0} tem {1} anos".format(nome, idade)) #Ao colocar o [0] estou definindo qual variavel sera colocada

#Versão de print "mais atual" versão 3.7

"""
int(idade) -> cast

Cast é a 'conversao' de um tipo de dado para outro.
"""
print(f"{nome} nasceu em {2019 - int(idade)}")
