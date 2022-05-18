import numpy as np
def Jacobi(A,b,k):
    n = A.shape[1]
    D = np.eye(n)
    D[np.arange(n),np.arange(n)] = A[np.arange(n),np.arange(n)]
    LU = D - A
    X = np.zeros(n)
    for i in range(k):
        D_inv = np.linalg.inv(D)
        X =  np.dot(np.dot(D_inv,LU),X) + np.dot(D_inv,b)
    return X

matrix2 = np.array([[9.6, 3.4, 4.5],
                  [1.7, 8.9, 3.7],
                  [2.4, 2.5, 7.4]])
y2 = np.array([2.1, 5.2, 1.1])

def solve_Jacobi():
    solve = Jacobi(matrix2, y2, 40)
    print("Jacobi")
    print(solve)


def Gauss_Seidel(A,b,k):
    n = A.shape[1]
    D = np.eye(n)
    D[np.arange(n),np.arange(n)] = A[np.arange(n),np.arange(n)]
    LU = D - A
    L = np.tril(LU)
    U = np.triu(LU)
    D_L = D - L
    X = np.zeros(n)
    for i in range(k):
        D_L_inv = np.linalg.inv(D_L)
        X =  np.dot(np.dot(D_L_inv,U),X) + np.dot(D_L_inv,b)
    return X

matrix3 = np.array([[9.6, 3.4, 4.5],
                  [1.7, 8.9, 3.7],
                  [2.4, 2.5, 7.4]])
y3 = np.array([2.1, 5.2, 1.1])

def solve_Gauss_Seidel():
    solve = Gauss_Seidel(matrix3, y3, 40)
    print("Gauss_Seidel")
    print(solve)

if __name__ == "__main__":
    solve_Jacobi()
    solve_Gauss_Seidel()