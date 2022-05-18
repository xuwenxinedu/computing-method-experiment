import numpy as np

def func(matrix):
    col = matrix.shape[1]  # 增广矩阵列数
    # 消元
    for i in range(col - 2):
        current_column = matrix[i:, i]
        max_index = np.argmax(current_column) + i
        if (matrix[max_index, i] == 0):
            break
        matrix[[i, max_index], :] = matrix[[max_index, i], :]
        l = matrix[i + 1:, i] / matrix[i, i]
        m = np.tile(matrix[i, :], (l.shape[0], 1)) * np.tile(l, (col, 1)).T
        matrix[i + 1:, :] = matrix[i + 1:, :] - m
    if (matrix[col - 2, col - 2] == 0):
        return
    x = np.zeros(col - 1)
    for i in range(col - 2, -1, -1):
        x[i] = (matrix[i, -1] - np.dot(matrix[i, :-1], x.T)) / matrix[i, i]
    return x

matrix = np.array([[1.6, 3.8, 4.5, 2.3],
                  [2.7, 2.9, 3.7, 1.2],
                  [4.3, 1.5, 2.4, -3.4]])

if __name__ == "__main__":
    solve = func(matrix)
    print(solve)
