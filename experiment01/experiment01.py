import math

class Binary:
    def __init__(self) -> None:
        pass
    
    def f(self, x):
        return math.log(x) + x**2 - 4
    
    def get_ans(self):
        e = 1e-6
        x1 = 0.1
        x2 = 10
        while True:
            mid = (x1 + x2) / 2
            if (abs(self.f(mid))) < e:
                print(mid)
                break
            elif self.f(mid) * self.f(x1) > 0:
                x1 = mid
            else:
                x2 = mid

class Newton:
    def __init__(self):
        pass

    def fa(self, x):
        return x**3 + 2 * x**2 + 10 * x - 20
    
    def fd(self, x):
        return 3 * x**2 + 4 * x + 10

    def get_ans(self, x0):
        cnt = 0
        x1 = x0 - self.fa(x0) / self.fd(x0)
        while abs(x1 - x0) >= 1e-6:
            cnt += 1
            x0 = x1
            x1 = x0 - self.fa(x0) / self.fd(x0)
            print(x1)
        return x1, cnt

def main():
    Binary().get_ans()
    print("===================")
    data = [-1, 1, 2]
    newton = Newton()
    for item in data:
        print("======000======")
        print(newton.get_ans(item))

if __name__ == "__main__":
    main()


