# Objetivo geral

Aprender a converter os tipos das variáveis.

## Convertendo tipos

Em alguns momentos será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:

Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

### Inteiro para float

```Python
preco = 10
print(preco)
>>> 10

preco = float(preco)
print(preco)
>>> 10.0

preco = 10/2
print(preco)
>>> 5.0
```

### Float para inteiro

```Python
preco =  10.30
print(preco)
>>> 10.3

preco = int(preco)
print(preco)
>>> 10
```

### Conversão por divisão

```Python
preco =  10
print(preco)
>>> 10

print(preco / 2)
>>> 5.0

print(preco // 2)
>>> 5
```

### Numérico para string

```Python
preco, idade = 10.50, 35

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco{preco}"
print(texto)
>>> Idade 35, preco 10.5
```

### String para número

```Python
preco = "10.50"
idade = "37"

print(float(preco))
>>>10.50

print(float(idade))
>>> 37
```

### Erro de conversão

```Python
preco = "Thiago"
print(float(preco))

>>>
Traceback (most recent call last):
	File "main.py", line 3, in <modulo>
		print(float(preco))
ValueError: could not convert string to float: 'Thiago'
```

