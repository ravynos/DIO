# Objetivo Geral

Conhecer os tipos de dados em Python.

## O que são tipos de dados?

### Por que usamos os tipos?

Os tipos servem para definir as características e comportamentos de um valor (objeto) para o interpretador.

Por exemplo: 

Com esse tipo eu sou capaz de realizar operações matemáticas.
Esse tipo para ser armazenado em memória irá consumir 24 bytes.

### Tipos em Python

Os tipos built-in são:

| Texto     | str (String)                 |
| --------- | ---------------------------- |
| Números   | int(Inteiro), float, complex |
| Sequência | list, tuple, range           |
| Mapa      | dict                         |
| Coleção   | set, frozenset               |
| Booleano  | bool                         |
| Binário   | bytes, bytearray, memoryview |
### Tipos numéricos

#### Números inteiros

Números inteiro são representados pelas classe **int** e possuem precisão ilimitada. São exemplos válidos de números inteiros:

1, 10, 100, -1, -10, -100 ...99001823

Números de ponto flutuantes

Os números de ponto flutuante são usados para representar os números racionais e sua implementação é feita pela classe **float**. São exemplos válidos de números de ponto flutuante:

1.5, -10.543, 0,76.... 999278.002

### Tipos Boleanos e Strings

#### Booleano

É usado para representar verdadeiro ou falso, e é implementado pela classe **bool**. Em Python o tipo booleano é uma subclasse de **int**, uma vez que qualquer número diferente de 0 representa verdadeiro e 0 representa falso. São exemplos válidos de booleanos:

True e False


#### Strings

Strings ou cadeia de caracteres são usadas para representar valores alfanuméricos, em Python as strings são definids utilizando a classe **str**. São exemplos válidos de string:

"Python", 'Python', """Python""", '''Python''', "p"

