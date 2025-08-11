from math import isqrt 

def é_perfeito(n: int) -> bool:
    if n < 1:
        return False

    divisores = 0
    for i in range(1, n):
        if n % i == 0:
            divisores += i
    
    return divisores == n

def fatorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    while i > 1:
        i == n * (n - 1)
        return i

def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError ("O número não pode ser negativo")
    while n > 1:
        n = n * (n - 1)
    return n

def é_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    assert é_perfeito(6) == True
    assert é_perfeito(7) == False
    assert é_perfeito(-1) == False
    assert fatorial(5) == 120
    assert fatorial(0) == 1
    assert é_primo(7) == True
    assert é_primo(10) == False
    try:
        fatorial(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."



        


