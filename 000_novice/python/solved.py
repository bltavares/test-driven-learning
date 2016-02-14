"""
Test Driven Learning Project.
Desenvolva TDD e programação com TDD e programação!
Módulo novice.

>>> __name__
'__main__'
"""


import functools
import operator


def negue(valor):
    """
    A função `negue` deve receber um valor boleano (verdadeiro ou falso) e
    retornar a negação desse valor.

    >>> negue(True)
    False
    >>> negue(False)
    True
    """

    return not valor


def diga_ola(nome):
    """A função `diga_ola` deve ser escrita de tal forma que receba como
    parâmetro um argumento *string*. Deve retornar a *string* "Olá, ", seguida
    do argumento recebido, mais um ponto final. A *string* recebida deve estar
    limpa, ou seja, sem caracteres de espaço no começo ou no fim. Se a *string*
    estiver vazia, retorna apenas "Olá!"

    >>> diga_ola('')
    'Olá!'
    >>> diga_ola('Paulo')
    'Olá, Paulo.'
    >>> diga_ola('  Paulo  ')
    'Olá, Paulo.'
    """

    if not nome:
        return 'Olá!'
    else:
        return 'Olá, {}.'.format(nome.strip())


def lista_numeros_pares(quantos):
    """A função `lista_numeros_pares` deve receber um parâmetro numérico
    inteiro que determina quantos números pares devem estar em um array que
    será o retorno da função.

    >>> lista_numeros_pares(0)
    []
    >>> lista_numeros_pares(1)
    [2]
    >>> lista_numeros_pares(4)
    [2, 4, 6, 8]
    >>> lista_numeros_pares(5)
    [2, 4, 6, 8, 10]
    >>> lista_numeros_pares(-1)
    []
    """

    return list(x for x in range(2, (quantos * 2) + 1) if x % 2 == 0)


def lista_multiplos(quantos, base):
    """A função `lista_multiplos` deve receber dois parâmetros numéricos
    inteiros e retornar uma lista de números inteiros. O tamanho da lista é
    determinado pelo primeiro parâmetro, e o número base será o segundo
    parâmetro.

    >>> lista_multiplos(0, 10)
    []
    >>> lista_multiplos(-1, 10)
    []
    >>> lista_multiplos(3, -1)
    [-3, -2, -1]
    >>> lista_multiplos(3, 0)
    []
    >>> lista_multiplos(3, 10)
    [10, 20, 30]
    """

    if base == 0:
        return []
    else:
        if base > 1:
            return list(x for x in range(base, (base * quantos) + 1, base))
        else:
            return list(x for x in range((base * quantos), base + 1, -base))


def soma(inteiros):
    """A função `soma` deve receber um *array* de números inteiros, e retornar
    a sua soma. Se a lista for vazia, deve retornar zero.

    >>> soma([])
    0
    >>> soma([1])
    1
    >>> soma([1, 2])
    3
    """

    return sum(inteiros)


def subtracao(inteiros):
    """A função `subtracao` deve receber um *array* de números inteiros, e
    retornar a subtração de todos os elementos em sequência. Por exemplo,
    subtracao([3,2,1]) deve retornar 0, e subtracao([10,2,3]) deve retornar 5.
    Se a lista for vazia, deve retornar zero.

    >>> subtracao([3, 2, 1])
    0
    >>> subtracao([10, 2, 3])
    5
    >>> subtracao([])
    0
    >>> subtracao([1, 2])
    -1
    >>> subtracao([-1, -2, -3])
    4
    """

    if len(inteiros) == 0:
        return 0
    else:
        return functools.reduce(operator.sub, inteiros)


def multiplicacao(inteiros):
    """A função `multiplicação` deve receber um *array* de números inteiros, e
    retornar o seu produto. Se a lista for vazia, deve retornar zero.

    >>> multiplicacao([1, 2, 3])
    6
    >>> multiplicacao([])
    0
    >>> multiplicacao([-2, 1, 4])
    -8
    >>> multiplicacao([-2, -1, 4])
    8
    """

    if len(inteiros) == 0:
        return 0
    else:
        return functools.reduce(operator.mul, inteiros)


def divisao(inteiros):
    """A função `divisao` deve receber um *array* de números inteiros, e
    retornar o resultado da sequência de divisões por cada elemento. Por
    exemplo, divisão([16, 4, 2]) deve retornar 2, e divisão([100,2,10]) deve
    retornar 5. Se a lista for vazia, deve retornar zero.

    >>> divisao([])
    0
    >>> divisao([0])
    0
    >>> divisao([16, 4, 2])
    2
    >>> divisao([100, 2, 10])
    5
    >>> divisao([0, 1])
    0
    >>> divisao([1, 0])
    Traceback (most recent call last):
    ...
        return functools.reduce(operator.floordiv, inteiros)
    ZeroDivisionError: integer division or modulo by zero

    """

    if len(inteiros) == 0:
        return 0
    else:
        return functools.reduce(operator.floordiv, inteiros)


def operacao(operador, inteiros):
    """A função `operacao` deve receber dois parâmetros. O primeiro parâmetro é
    um caractere indicando a operação aritmética básica a ser realizada ('+',
    '-', '\*', '/'). O segundo parâmetro é um *array* de números inteiros, para
    os quais a operação deve ser aplicada. A função deve retornar o resultado
    da operação no *array*. Chame as funções já criadas para cada operação. Em
    caso de operação inválida, gere uma exceção.

    >>> operacao('+', [1, 2])
    3
    >>> operacao('-', [1, 2])
    -1
    >>> operacao('*', [1, 2])
    2
    >>> operacao('/', [1, 2])
    0
    >>> operacao('=', [1, 2])
    Traceback (most recent call last):
    ...
    Exception: Operador inválido
    """

    operacoes = {
        '+': soma,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao,
    }

    try:
        return operacoes[operador](inteiros)
    except KeyError:
        raise Exception('Operador inválido')


def maior(inteiros):
    """A função `maior` deve receber um *array* de números inteiros e retornar
    qual é o maior deles.

    >>> maior([0, 1 ,100])
    100
    >>> maior([0])
    0
    >>> maior([])
    Traceback (most recent call last):
    ...
    ValueError: max() arg is an empty sequence

    """

    return max(inteiros)


def intersecao(a, b):
    """A função `intersecao` deve receber dois *arrays* contendo números
    inteiros, e retornar a interseção entre os conjuntos, ou seja, um *array*
    que contenha apenas os números que estejam contidos nos dois *arrays*
    passados para a função.

    >>> intersecao([], [])
    []
    >>> intersecao([1, 2], [3, 4])
    []
    >>> intersecao([1, 2], [2, 3])
    [2]
    """

    return list(set(a).intersection(set(b)))


if __name__ == "__main__":
    """Se executar o script, os testes serão executados."""

    import doctest

    doctest.testmod(verbose=True)
