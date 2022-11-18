import math


# Função para sumar 2 valores
def sum(val1, val2):
    return val1 + val2


# Função para subtrair 2 valores
def subtraction(val1, val2):
    return val1 - val2


# Função para multiplicar 2 valores
def multiply(val1, val2):
    return val1 * val2

# Função para dividir 2 valores
def div(val1, val2):
    if val2 != 0:
        return val1 / val2
    else:
        return "Divisor tem que ser diferente de 0"

# Função para fazer a potencia do val1 por val2
def pow(val1, val2):
    return pow(val1, val2)

# Função para a raiz quadrada de um valor
def square_root(val):
    if val >= 0:
        return math.sqrt(val)
    else:
        return "Número introduzido deve ser maior que 0"

# Função para calcular a percentagem de um valor
def percentage(val):
    return val * 100
