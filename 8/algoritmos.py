import numpy as np

def f_atv1(T, E, K):
    """Função para a Atividade 1: f(T) = 5.67e-8 * T^4 + 0.4 * (T - K) - E"""
    sigma = 5.67e-8
    return sigma * T**4 + 0.4 * (T - K) - E

def bissecao(func, a, b, E, K, tol=1e-7, max_iter=100):
    """Método da Bisseção para encontrar a raiz de func(T, E, K) = 0."""
    if func(a, E, K) * func(b, E, K) >= 0:
        print("Erro: O método da bisseção requer que f(a) e f(b) tenham sinais opostos.")
        return None

    iter_count = 0
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        f_c = func(c, E, K)
        if f_c == 0:
            return c
        elif func(a, E, K) * f_c < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2.0

def g_atv1(T, E, K):
    """
    Função g(T) para Ponto Fixo na Atividade 1 (Usando o rearranjo mais estável).
    T = h(T) = [ (E + 0.4 * K - 0.4 * T) / (5.67e-8) ]^(1/4)
    """
    sigma = 5.67e-8
    
    numerador = E + 0.4 * K - 0.4 * T
    
    if numerador < 0:
        return (numerador / sigma)**(1/4) 

    return (numerador / sigma)**(1/4)

def ponto_fixo(g, x0, E, K, tol=1e-7, max_iter=100):
    """Método do Ponto Fixo para encontrar a raiz de T = g(T, E, K)."""
    x = x0
    iter_count = 0
    for _ in range(max_iter):
        x_new = g(x, E, K)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
        iter_count += 1
    print(f"Aviso: Ponto Fixo não convergiu em {max_iter} iterações.")
    return x

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    """
    Resolve o sistema Ax = b usando o método de Gauss-Seidel.
    A: matriz de coeficientes (numpy array).
    b: vetor de termos independentes (numpy array).
    x0: vetor de chute inicial (numpy array).
    """
    n = A.shape[0]
    x = x0.copy()
    
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i]) 
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            
            if A[i, i] == 0:
                print("Erro: Elemento diagonal zero. A matriz pode não ser diagonalmente dominante.")
                return None

            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new

        x = x_new
    
    print(f"Aviso: Gauss-Seidel não convergiu em {max_iter} iterações.")
    return x

def F_atv4(T, E1, E2):
    """Vetor de funções F(T) para a Atividade 4."""
    T1, T2 = T
    f1 = (T1**4 + 0.06823 * T1) - (T2**4 + 0.05848 * T2) - E1
    f2 = (T1**4 + 0.05848 * T1) - (2 * T2**4 + 0.11696 * T2) - E2
    return np.array([f1, f2])

def J_atv4(T):
    """Matriz Jacobiana J(T) para a Atividade 4."""
    T1, T2 = T
    
    df1_dT1 = 4 * T1**3 + 0.06823

    df1_dT2 = -(4 * T2**3 + 0.05848)
    
    df2_dT1 = 4 * T1**3 + 0.05848

    df2_dT2 = -(8 * T2**3 + 0.11696)
    
    return np.array([
        [df1_dT1, df1_dT2],
        [df2_dT1, df2_dT2]
    ])

def newton_raphson_sistemas(F, J, x0, E1, E2, tol=1e-6, max_iter=50):
    """
    Método de Newton-Raphson para resolver F(x) = 0.
    F: função que retorna o vetor F(x).
    J: função que retorna a matriz Jacobiana J(x).
    x0: vetor de chute inicial (numpy array).
    """
    x = x0.copy()
    
    for k in range(max_iter):
        F_k = F(x, E1, E2)
        J_k = J(x)
        
        try:
            delta_x = np.linalg.solve(J_k, -F_k)
        except np.linalg.LinAlgError:
            print("Erro: Matriz Jacobiana singular.")
            return None
        
        x_new = x + delta_x
        
        if np.linalg.norm(delta_x, ord=np.inf) < tol:
            return x_new

        x = x_new
    
    print(f"Aviso: Newton-Raphson não convergiu em {max_iter} iterações.")
    return x