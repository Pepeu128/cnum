import numpy as np
import matplotlib.pyplot as plt

from algoritmos import regressao


def plot(x, y, v, num_img=1):
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    y_vals = np.zeros_like(x_vals, dtype=float)
    A = regressao(x, y, v)
    for p, ap in enumerate(A):
        y_vals += ap * (x_vals**p)
    plt.figure(figsize=(7, 4))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="red", label="Ajuste linear f(x)")
    plt.title("Ajuste linear por mínimos quadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"10/regressao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()


def main():

    print("\n-- Atividade 1 --")

    x = np.array([-0.35, 0.15, 0.23, 0.35], dtype=float)
    y = np.array([0.20, -0.50, 0.54, 0.70], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plot(x, y, v, 1)

    print("\n-- Atividade 2 --")
    
    x = np.array([-1.94, -1.44, 0.93, 1.39], dtype=float)
    y = np.array([1.02, 0.59, -0.28, -1.04], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plot(x, y, v, 2)

    print("\n-- Atividade 3 --")
    
    x = np.array([0.01, 1.02, 2.04, 2.95, 3.55], dtype=float)
    y = np.array([1.99, 4.55, 7.20, 9.51, 10.82], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plot(x, y, v, 3)

    print("--- Atividade 4 ---")
    
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], dtype=float)
    y = np.array([31, 35, 37, 33, 28, 20, 16, 15, 18, 23, 31], dtype=float)
    
    print("\nItem a) Ajuste Trigonométrico")
    
    v_a = lambda x: np.column_stack((
        np.ones(len(x)),        
        np.sin(2 * np.pi * x),  
        np.cos(2 * np.pi * x)   
    ))
    
    A_a = regressao(x, y, v_a)
    
    print(f"Coeficientes encontrados:")
    print(f"a = {A_a[0]:.6f}")
    print(f"b = {A_a[1]:.6f}")
    print(f"c = {A_a[2]:.6f}")
    print(f"Função: f(x) = {A_a[0]:.4f} + {A_a[1]:.4f}*sin(2πx) + {A_a[2]:.4f}*cos(2πx)")
    
    plot_ajuste(x, y, v_a, A_a, 
                "Atividade 4a: Ajuste Trigonométrico", 
                "atividade4_a.png")

    print("\nItem b) Ajuste Polinomial Cúbico")
    
    v_b = lambda x: np.column_stack((
        np.ones(len(x)), 
        x,               
        x**2,            
        x**3             
    ))
    
    A_b = regressao(x, y, v_b)
    
    print(f"Coeficientes encontrados:")
    print(f"a = {A_b[0]:.6f}")
    print(f"b = {A_b[1]:.6f}")
    print(f"c = {A_b[2]:.6f}")
    print(f"d = {A_b[3]:.6f}")
    print(f"Função: f(x) = {A_b[0]:.4f} + {A_b[1]:.4f}x + {A_b[2]:.4f}x^2 + {A_b[3]:.4f}x^3")
    
    plot_ajuste(x, y, v_b, A_b, 
                "Atividade 4b: Ajuste Polinomial Cúbico", 
                "atividade4_b.png")

if __name__ == "__main__":
    main()
