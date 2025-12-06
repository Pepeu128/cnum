import numpy as np
import algoritmos as alg

X_interp = np.array([4.9, 3.3, 3.0, 2.0]) 
Y_interp = np.array([1.75, 2.5, 2.75, 3.2]) 

I_exp = np.array([0.5, 1.1, 1.5, 2.2, 2.5, 3.1]) 
V_exp = np.array([5.1, 10.3, 15.2, 20.1, 24.7, 30.5]) 

t_rl = np.array([0.0, 0.1, 0.2, 0.3, 0.4]) 
i_rl = np.array([0.00, 0.82, 1.36, 1.60, 1.73]) 
L_indutor = 0.1 

Raio_Max = 4.0
def funcao_vazao(r):
    velocidade = 3 * (1 - r/Raio_Max)**(0.25)
    return 2 * np.pi * r * velocidade


def atividade_1():
    print("\n--- Atividade 1: Interpolação (Ponto A) ---")
    x_alvo = 1.1 
    res = alg.lagrange(X_interp, Y_interp, x_alvo)
    print(f"Interpolado em x={x_alvo}: {res:.6f}")

def atividade_2():
    print("\n--- Atividade 2: Interpolação (Ponto B ou Inversa) ---")
    x_alvo = 1.3 
    res = alg.lagrange(X_interp, Y_interp, x_alvo)
    print(f"Interpolado em x={x_alvo}: {res:.6f}")

def atividade_3():
    print("\n--- Atividade 3: Ajuste Mínimos Quadrados (Cálculo dos Coeficientes) ---")
    a, b = alg.mmq_linear(I_exp, V_exp)
    print(f"Coeficientes ajustados:")
    print(f"a (inclinação) = {a:.6f}")
    print(f"b (intercepto) = {b:.6f}")

def atividade_4():
    print("\n--- Atividade 4: Interpretação Física (Lei de Ohm) ---")
    R, k = alg.mmq_linear(I_exp, V_exp)
    print(f"Equação: V = {R:.6f}*I + {k:.6f}")
    print(f"Resistência (R) = {R:.8f} Ohms")
    print(f"Constante (k)   = {k:.8f} Volts")
    return R

def atividade_5(R):
    print("\n--- Atividade 5: Circuito RL (Diferença Progressiva) ---")
    idx = 0 
    didt = alg.dp(t_rl, i_rl, idx)
    v_t = L_indutor * didt + R * i_rl[idx]
    
    print(f"Tempo t = {t_rl[idx]}")
    print(f"di/dt (Progressiva) = {didt:.6f}")
    print(f"Tensão V(t) = {v_t:.6f}")

def atividade_6(R):
    print("\n--- Atividade 6: Circuito RL (Diferença Regressiva) ---")
    idx = 2 
    didt = alg.dr(t_rl, i_rl, idx)
    v_t = L_indutor * didt + R * i_rl[idx]
    
    print(f"Tempo t = {t_rl[idx]}")
    print(f"di/dt (Regressiva) = {didt:.6f}")
    print(f"Tensão V(t) = {v_t:.6f}")

def atividade_7(R):
    print("\n--- Atividade 7: Circuito RL (Diferença Central) ---")
    idx = 2
    didt = alg.dc(t_rl, i_rl, idx)
    v_t = L_indutor * didt + R * i_rl[idx]
    
    print(f"Tempo t = {t_rl[idx]}")
    print(f"di/dt (Central) = {didt:.6f}")
    print(f"Tensão V(t) = {v_t:.6f}")

def atividade_8():
    print("\n--- Atividade 8: Integração Vazão (Ponto Médio) ---")
    n = 10 
    q = alg.integral_pm(funcao_vazao, 0, Raio_Max, n)
    print(f"Vazão Q (Ponto Médio, n={n}) = {q:.6f}")

def atividade_9():
    print("\n--- Atividade 9: Integração Vazão (Trapézio) ---")
    n = 10
    q = alg.integral_trap(funcao_vazao, 0, Raio_Max, n)
    print(f"Vazão Q (Trapézio, n={n})    = {q:.6f}")

def atividade_10():
    print("\n--- Atividade 10: Integração Vazão (Simpson) ---")
    n = 10
    q = alg.integral_simp(funcao_vazao, 0, Raio_Max, n)
    print(f"Vazão Q (Simpson, n={n})     = {q:.6f}")

def main():
    print("=== EXECUTANDO TRABALHO 13 ===")
    
    atividade_1()
    atividade_2()
    
    atividade_3()
    R_calculado = atividade_4() 