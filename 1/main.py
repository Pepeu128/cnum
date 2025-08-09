
from math import sqrt

def zeros(a, b, c):

    if a == 0:
        if b == 0:
            raise ValueError("A equação não é de segundo grau")
        else:
            return [-c/b]

    delta = b**2 - (4*a*c)

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return [x, x]
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return [x1, x2]

def main():
    x = zeros(6, -5, 3)
    print(x)

if __name__ == "__main__":
    main()