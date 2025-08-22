from math import isqrt 
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])

C = A @ B

def plot(n: int) -> None:
    x = np.linspace(-np.pi, np.pi, n)  
    y_sen = np.sin(x)                   
    y_cos = np.cos(x)                   

    plt.plot(x, y_sen, label='seno')
    plt.plot(x, y_cos, label='cosseno')
    plt.xlim(-np.pi, np.pi)

    plt.xlabel('Ângulo [rad]')
    plt.ylabel('Função trigonométrica(x)')
    plt.grid(True)
    plt.legend()
    plt.savefig("plot.png")  # Salva como imagem no ambiente

    print(f'x =\n{x}')
    print(f'y_sen =\n{y_sen}')
    print(f'y_cos =\n{y_cos}')

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

def soma_digitos(n: int) -> int:
    soma = 0
    while n > 0:
        soma += n % 10
        n //= 10
    return soma

if __name__ == "__main__":
    def main():
        assert is_perfect(6) == True
        assert is_perfect(7) == False
        assert is_perfect(-1) == False
        assert factorial(5) == 120
        assert factorial(0) == 1
        try:
            factorial(-1)
        except ValueError as error:
            assert str(error) == "O número deve ser não negativo."
        assert is_prime(7) == True
        assert is_prime(10) == False
        assert sum_of_digits(123) == 6
        try:
            sum_of_digits(-1)
        except ValueError as error:
            assert str(error) == "O número deve ser não negativo."
    print(C)
    print(C.shape) 
    print(C.size) 
    print(len(C)) 
    plot(35)



        


