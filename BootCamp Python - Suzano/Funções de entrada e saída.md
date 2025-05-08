
# Objetivo Geral

Aprender como receber e exibir informações para o usuário.

## Lendo valores com a função input

### Função input

A função builtin é utilizada quando queremos ler dados da entrada padrão  (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela).  A função lê a entrada, converte para string e retorna o valor.

Exemplo

```Python
nome = input("Informe seu nome: ")
>>> Informe seu nome: |
```


## Exibindo valores com a função print

### Função print

A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.


Exemplo

```Python
nome = "Thiago"
sobrenome = "Sobrinho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

>>> Thiago Sobrinho
>>> Thiago Sobrinho...
>>> Thiago#Sobrinho
```

