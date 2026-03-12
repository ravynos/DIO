nome = "Thiago"
idade = 38
profissão = "Programador"
linguagem = "Python"

#Old style %
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissão, linguagem))

"""Olá, me chamo Thiago. Eu tenho 38 anos de idade, trabalho como Programador e estou matriculado no curso de Python"""

#Metodo Format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissão, linguagem))

# Pode ser definido dentro dos colchetes, qual a posição da variável você deseja imprimir.
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem, profissão, idade, nome))

# Metodo F-string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso de {linguagem}.")