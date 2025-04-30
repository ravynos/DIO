# Usando o modo interativo

## O modo interativo

O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora.

## Iniciando o Modo Interativo

Existem duas formas de iniciar o modo interativo, chamando apenas o interpretador (python) ou executando o script com a flag -i (python -i app.py).

# Funções dir e help

## dir

Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto. Exemplo:

dir()
dir(100)

## help

Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informa por parâmetro qual o nome do módulo, função, classe, método ou variável. Exemplo: 

help()
help(100)