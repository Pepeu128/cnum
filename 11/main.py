import numpy as np
from scipy.differentiate import derivative

from algoritmos import dp, dr, dc

def dp_array(y, i, h):
    return (y[i + 1] - y[i]) / h

def dr_array(y, i, h):
    return (y[i] - y[i - 1]) / h

def dc_array(y, i, h):
    return (y[i + 1] - y[i - 1]) / (2 * h)

def main():
    print("-- Atividade 1 --")

    h1 = 1e-2
    h2 = 1e-3
    eps = np.finfo(float).eps

    print("f(x) = sin(x)")

    f = lambda x: np.sin(x)

    print("Diferença progressiva:")
    print("h = 0.01 | f'(x)=", dp(f, 2, h1))
    print("h = 0.001 | f'(x)=", dp(f, 2, h2))
    print("h = eps | f'(x)=", dp(f, 2, np.sqrt(eps)))

    print("Diferença regressiva:")
    print("h = 0.01 | f'(x)=", dr(f, 2, h1))
    print("h = 0.001 | f'(x)=", dr(f, 2, h2))
    print("h = eps | f'(x)=", dr(f, 2, np.sqrt(eps)))

    print("Diferença central:")
    print("h = 0.01 | f'(x)=", dc(f, 2, h1))
    print("h = 0.001 | f'(x)=", dc(f, 2, h2))
    print("h = eps | f'(x)=", dc(f, 2, eps ** (1 / 3)))

    print("Derivada com SciPy:")
    r = derivative(f, 2)
    print("f'(x)=", r.df)

    fd = lambda x: np.cos(x)
    print("Derivada analítica:")
    print("f'(x) = cos(x)")
    print("f'(x)=", fd(2))

    print("f(x) = e^(-x)")

    f = lambda x: np.exp(-x)

    print("Diferença progressiva:")
    print("h = 0.01 | f'(x)=", dp(f, 1, h1))
    print("h = 0.001 | f'(x)=", dp(f, 1, h2))
    print("h = eps | f'(x)=", dp(f, 1, np.sqrt(eps)))

    print("Diferença regressiva:")
    print("h = 0.01 | f'(x)=", dr(f, 1, h1))
    print("h = 0.001 | f'(x)=", dr(f, 1, h2))
    print("h = eps | f'(x)=", dr(f, 1, np.sqrt(eps)))

    print("Diferença central:")
    print("h = 0.01 | f'(x)=", dc(f, 1, h1))
    print("h = 0.001 | f'(x)=", dc(f, 1, h2))
    print("h = eps | f'(x)=", dc(f, 1, eps ** (1 / 3)))

    print("Derivada com SciPy:")
    r = derivative(f, 1)
    print("f'(x)=", r.df)

    fd = lambda x: -np.exp(-x)
    print("Derivada analítica:")
    print("f'(x) = e^(-x)")
    print("f'(x)=", fd(1))

    print("-- Atividade 2 --")

    vi = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    vo = np.array([0.0, 1.05, 1.83, 2.69, 3.83, 4.56, 5.49, 6.56, 6.11, 7.06, 8.29])
    
    h = 0.5 

    pontos_interesse = [
        {"val": 1.0, "idx": 2},
        {"val": 4.5, "idx": 9}
    ]

    print(f"{'Caso (Vi)':<10} | {'a. Prog':<10} | {'b. Regr':<10} | {'c. Cent':<10} | {'d. M.Quad':<10}")
    print("-" * 65)

    A = np.vstack([vi, vi**3]).T
    
    coeffs, _, _, _ = np.linalg.lstsq(A, vo, rcond=None)
    a1, a3 = coeffs
    
    def ganho_analitico(v):
        return a1 + 3 * a3 * (v**2)

    for pt in pontos_interesse:
        v_val = pt["val"]
        idx = pt["idx"]

        res_a = dp_array(vo, idx, h)
        res_b = dr_array(vo, idx, h)
        res_c = dc_array(vo, idx, h)
        
        res_d = ganho_analitico(v_val)

        print(f"Vi = {v_val:<5} | {res_a:<10.2f} | {res_b:<10.2f} | {res_c:<10.2f} | {res_d:<10.2f}")

    print("-" * 65)
    print("Compare com as Respostas Esperadas (Página 5 do PDF):")
    print("Vi=1.0 -> a: 1.72, b: 1.56, c: 1.64, d: 1.86")
    print("Vi=4.5 -> a: 2.46, b: 1.90, c: 2.18, d: 1.14")

if __name__ == "__main__":
    main()
