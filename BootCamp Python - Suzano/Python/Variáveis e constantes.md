# Objetivo Geral

Entender o que são e como utilizar variáveis e constantes.

## O que são variáveis e constantes?

### Variáveis

Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

```Python
idade = 37
nome = 'Thiago'
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')
>>> Meu nome é Thiago e eu tenho 37 anos de idade.

idade, nome = (37, 'Thiago')
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')
>>> Meu nome é Thiago e eu tenho 37 anos de idade.
```

#### Alterando os valores

Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma atribuição de um novo valor:

```Python
idade, nome = (37, 'Thiago')
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')
>>> Meu nome é Thiago e eu tenho 37 anos de idade.

idade, nome = (4, 'Ayra')
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')
>>> Meu nome é Ayra e eu tenho 4 anos de idade.
```

### Constantes

Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.

#### Python não tem constantes

Não existe uma palavra reservada para informa ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.

Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letra maiúsculas: 

```Python
ABS_PATH = 'C:/PROJETOS/DIO/PYTHON'
DEBUG = TRUE
ESTADOS = ['SP', 'RJ', 'MG']
AMOUNT = 30.2
```

## Boas práticas

- O padrão de nomes deve ser snake case.
- Escolher nomes sugestivos.
- Nomes de constantes em maiúsculo.

