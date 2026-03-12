# Manipulando strings.

#Maiúscula, minúscula e título.

curso = "pYtHon"

#Converte o resultado da string toda para Maiúsculo.
print(curso.upper())
"""PYTHON"""

#Converte para minúsculo.
print(curso.lower())
"""python"""

#Convete para a primeira letra Maiúscula e o resto minúsculo.
print(curso.title())
"""Python"""

#Eliminando espaços em branco

curso = "    Python  "

#Elimina todos os espaços em branco
print(curso.strip())
"""Python"""

#Elimina os espaços em branco a esquerda.
print(curso.lstrip())
"""Python  """

#Elimina os espaços em branco a direira.
print(curso.rstrip())
"""     Python"""

# Junções e centralização

curso = "Python"

#Centraliza a string, permitindo assim 2 argumentos, a quantidade de caracteres, no exemplo, 10 caracteres, e o argumento opcional
#do preenchimento, caso não seja definido, será adicionado espaços em branco.
print(curso.center(10, "#"))
"""##Python##"""

#Vai ser feita a junção do caracter definido, e com isso, ele vai fazer a leitura de cada caracter da string e adicionar o item definido.
print(".".join(curso))
"""P.y.t.h.o.n"""

