from math import sqrt 

def é_perfeito(n: int) -> bool:
    if n < 1:
        return False

    divisores = 0
    for i in range(1, n):
        if n % i == 0:
            divisores += i
    
    return divisores == n

def fatorial(n: int) -> int:
    for n in range(n, 1):
        if n == 0:
            return False
        if (n - 1) == 0:
            return n
        else:
            return n * fatorial(n - 1)

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
    if sqrt(n) == int:
        return False
    if (n > 2) / 2 == int:
        return False 
    
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def main():
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert is_prime(7) == True
    assert is_prime(10) == False
    try:
        factorial(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."



        


