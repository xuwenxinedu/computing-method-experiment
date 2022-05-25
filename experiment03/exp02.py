from scipy import interpolate



def f(x):
    return 1 / (1 + 25 * (x**2))


    

def main():
    x = []
    y = []
    for i in range(11):
        x.append(-1 + 0.2 * i)
        y.append(f(x[len(x) - 1]))
    l = interpolate.PchipInterpolator(x, y)
    x_new = []
    for j in range(1, 21):
        xj = 0.05 * j
        x_new.append(xj)
    ans = l(x_new)
    print(ans)

main()