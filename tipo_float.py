"""
Tipo Float = Tipo Real ou Tipo Decimal
É o tipo que possui casas decimais.

OBS: O separador de casas decimais é o ponto "." e não a vírgula ",".
"""

# Errado
valor = 1,44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer uma dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor2))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
""" 5j é um número complexo

variavel = 5j
print(type(variavel))

"""
variavel = 5j
print(type(variavel))