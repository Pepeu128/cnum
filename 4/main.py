
import numpy as np
import matplotlib.pyplot as plt

from algoritmos import bissecao

def f1(x):
    return x**3 - x - 2

def f2(x):
    return x**(1/2) - np.cos(x)

def plot(f, xi, xf, d=0.1, num_img=1):
    x_vals = np.arange(xi, xf, d)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)  # eixo x
    plt.axvline(0, color="black", linewidth=1)  # eixo y
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.title("Visualização da função f(x)")

    plt.savefig(f"4/bissecao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()

def main():
    # Atividade 1
    print("-- Atividade 1 --")
    plot(f1, -1, 2, num_img=1)
    r, i = bissecao(f1, 1, 2, 1e-15)
    print(f"raiz = {r} , i = {i}")
    # Atividade 2
    print("-- Atividade 2 --")
    plot(f2, 0, 1, num_img=2)
    r, i = bissecao(f2, 0, 1, 1e-4, iter=4)
    print(f"raiz = {r} , i = {i}")

if __name__ == "__main__":
    main()
