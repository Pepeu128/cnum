import numpy as np

def lagrange(x, y, x_int):
    """
    Calcula o valor interpolado em x_int usando o Polinômio de Lagrange.
    """
    n = len(x)
    soma = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x_int - x[j]) / (x[i] - x[j])
        soma += y[i] * L
    return soma

def minimos_quadrados_linear(x, y):
    """
    Ajusta uma reta y = ax + b (ou V = R*I + k) aos pontos.
    Retorna os coeficientes a (inclinação) e b (intercepto).
    """
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)

    denom = n * sum_x2 - sum_x ** 2
    a = (n * sum_xy - sum_x * sum_y) / denom
    b = (sum_x2 * sum_y - sum_x * sum_xy) / denom
    
    return a, b

def diff_progressiva(x, y, i):
    """Derivada usando o ponto atual (i) e o próximo (i+1)."""
    return (y[i+1] - y[i]) / (x[i+1] - x[i])

def diff_central(x, y, i):
    """Derivada usando o ponto anterior (i-1) e o próximo (i+1)."""
    return (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])

def integral_ponto_medio(f, a, b, n):
    """Regra do Ponto Médio Composta."""
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    return h * np.sum(f(x))

def integral_trapezio(f, a, b, n):
    """Regra do Trapézio Composta."""
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def integral_simpson(f, a, b, n):
    """Regra de Simpson 1/3 Composta."""
    if n % 2 != 0: n += 1 
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])