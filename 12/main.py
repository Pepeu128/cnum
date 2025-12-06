import numpy as np
from scipy.integrate import quad

from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
)


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    a = 0
    b = 1

    print("f(x) = e^(-x)")
    f = lambda x: np.exp(-x)
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")

    print("\n" + "="*40)
    print("ATIVIDADE 2")
    print("="*40)
    
    f3 = lambda x: np.exp(x - x**2)
    a, b = 2, 3
    nome_f3 = "e^(x - x^2)"
    
    ref3, _ = quad(f3, a, b)
    
    print(f"Calculando integral de {nome_f3} no intervalo [{a}, {b}]")
    print(f"Valor exato (SciPy): {ref3:.8f}\n")
    
    num_divisoes = [4, 10, 100]

    print(f"{'N (Divisões)':<12} | {'Método':<10} | {'Resultado':<12} | {'Erro':<12}")
    print("-" * 60)

    for N in num_divisoes:
        passo = (b - a) / N 
        
        res_m = integral(medio, f3, a, b, n=passo)
        res_t = integral(trapezio, f3, a, b, n=passo)
        res_s = integral(simpson, f3, a, b, n=passo)

        print(f"{N:<12} | {'Médio':<10} | {res_m:.8f}   | {abs(res_m - ref3):.2e}")
        print(f"{'':<12} | {'Trapézio':<10} | {res_t:.8f}   | {abs(res_t - ref3):.2e}")
        print(f"{'':<12} | {'Simpson':<10} | {res_s:.8f}   | {abs(res_s - ref3):.2e}")
        print("-" * 60)

if __name__ == "__main__":
    main()
