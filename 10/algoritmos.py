import numpy as np

def regressao(x, y, v):

    V = v(x)
    
    Vt = V.T
    
    term1 = np.linalg.inv(Vt @ V)
    term2 = Vt @ y
    
    A = term1 @ term2
    
    return A