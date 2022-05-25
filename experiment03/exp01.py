import numpy as np

def f(x):
    return 1 / (1 + 25 * (x**2))

def lagrange(x,y,w):
    n = len(x)
    res=0
    for i in range(n):
        temp = 1 
        for j in range(n):
            if i!=j: temp = temp * (w-x[j]) / (x[i] - x[j]) 
        res += temp * y[i]
    return res



def main():
    x = []
    y = []
    for i in range(11):
        x.append(-1 + 0.2 * i)
        y.append(f(x[len(x) - 1]))
    # print(x)
    # print(y)
    ans = []
    for j in range(1, 21):
        xj = 0.05 * j
        ans.append(format(lagrange(x, y, xj), '.4f'))
    print(ans)

    



if __name__ == "__main__":
    main()