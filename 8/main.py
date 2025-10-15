# main.py

import numpy as np
from algoritmos import bissecao, ponto_fixo, f_atv1, g_atv1, gauss_seidel, newton_raphson_sistemas, F_atv4, J_atv4

print("--- Atividade 1: Temperatura Mínima da Placa (Método da Bisseção) ---")
E = 500.125
K = 272.975
T_chute = 300.0  
a = 300.0
b = 400.0
T_bissecao = bissecao(f_atv1, a, b, E, K, tol=1e-8)
print(f"Parâmetros: E={E}, K={K}")
print(f"Resposta aproximada (Bisseção): T={T_bissecao:.18f}")
print("\n")
T_ponto_fixo = ponto_fixo(g_atv1, T_chute, E, K, tol=1e-8)
print(f"--- Atividade 1: Temperatura Mínima da Placa (Método do Ponto Fixo) ---")
print(f"Resposta aproximada (Ponto Fixo): T={T_ponto_fixo:.18f}")
print("\n")
print("--- Atividade 2: Tensões Nominais dos Reatores (Gauss-Seidel) ---")
A2 = np.array([
    [17.0, -2.0, -3.0],
    [-5.0, 21.0, -2.0],
    [-5.0, -5.0, 22.0]
])
b2 = np.array([500.0, 200.0, 300.0])
x0_2 = np.array([0.0, 0.0, 0.0]) 

R_gauss_seidel = gauss_seidel(A2, b2, x0_2, tol=1e-6)

if R_gauss_seidel is not None:
    R1 = R_gauss_seidel[0]
    R2 = R_gauss_seidel[1]
    R3 = R_gauss_seidel[2]
    print(f"R1 = {R1:.8f}")
    print(f"R2 = {R2:.8f}")
    print(f"R3 = {R3:.8f}")
print("\n")
print("--- Atividade 3: Corrente no Resistor R3 (Gauss-Seidel) ---")
A3 = np.array([
    [20.0, 10.0],
    [10.0, 20.0]
])
b3 = np.array([100.0, 100.0])
x0_3 = np.array([0.0, 0.0])

I_gauss_seidel = gauss_seidel(A3, b3, x0_3, tol=1e-6)

if I_gauss_seidel is not None:
    I1 = I_gauss_seidel[0]
    I2 = I_gauss_seidel[1]
    
    A_correto = np.array([
        [ 20.0, -10.0],
        [-10.0,  20.0]
    ])
    I_correto = gauss_seidel(A_correto, b3, x0_3, tol=1e-6)
    
    if I_correto is not None:
        I1_c = I_correto[0]
        I2_c = I_correto[1]
        I_R3 = I1_c - I2_c
        
        print(f"Sistema Corrigido (Malhas): I1={I1_c:.8f}, I2={I2_c:.8f}")
        print(f"Corrente no R3: IR3 = I1 - I2 = {I_R3:.4f} A")
print("\n")
print("--- Atividade 4: Temperaturas de Equilíbrio (Newton-Raphson para Sistemas) ---")
E1 = 0.01753
E2 = 0.00254
x0_4 = np.array([0.3, 0.2]) 

T_newton = newton_raphson_sistemas(F_atv4, J_atv4, x0_4, E1, E2, tol=1e-6)

if T_newton is not None:
    T1 = T_newton[0]
    T2 = T_newton[1]
    print(f"T1 = {T1:.5f}")
    print(f"T2 = {T2:.6f}")