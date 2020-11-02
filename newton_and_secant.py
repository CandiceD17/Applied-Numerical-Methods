import math
import numpy as np
import matplotlib.pyplot as plt


def f(x, derivative = 0):
    if derivative == 0:
        return math.exp(x) + pow(2, -x) + 2 * math.cos(x) - 6
    elif derivative == 1:
        return math.exp(x) - np.log(2) * pow(2, -x) - 2 * math.sin(x)
    elif derivative == 2:
        return math.exp(x) + np.log(2) * pow(2, -x) - 2 * math.cos(x)


def newton(p0, tol, maxIter):
    p = p0
    ps = [p0]
    index = [0]
    for i in range(1, maxIter+1):
        p = p - f(p) / f(p, 1)
        if abs(f(p)) < tol or abs(p - ps[-1]) < tol:
            ps.append(p)
            index.append(i)
            return p, ps, index
        ps.append(p)
        index.append(i)
    return p, ps, index


def secant(p0, p1, tol, maxIter):
    p = p1
    ps = [p0, p1]
    print(p1)
    index = [0]
    for i in range(1, maxIter+1):
        p = p - f(p) * (p - ps[-2]) / (f(p) - f(ps[-2]))
        if abs(f(p)) < tol or abs(p - ps[-1]) < tol:
            ps.append(p)
            index.append(i)
            return p, ps, index
        ps.append(p)
        index.append(i)
    return p, ps, index

def modified_newton(p0, tol, maxIter):
    p = p0
    ps = [p0]
    index = [0]
    for i in range(1, maxIter+1):
        p = p - f(p) * f(p, 1) / (pow(f(p, 1), 2) - f(p) * f(p, 2))
        if abs(f(p)) < tol or abs(p - ps[-1]) < tol:
            ps.append(p)
            index.append(i)
            return p, ps, index
        ps.append(p)
        index.append(i)
    return p, ps, index


def main():
    p_n, ps_n, index_n = newton(2, 1e-8, 100)
    p_s, ps_s, index_s = secant(2, ps_n[1], 1e-8, 100)
    p_m, ps_m, index_m = modified_newton(2, 1e-8, 100)
    ps_s.pop(1)
    plt.plot(index_n, ps_n, label = "Newton's Method")
    plt.plot(index_s, ps_s, label = "secant method")
    plt.plot(index_m, ps_m, label = "Modified Newton's Method")
    plt.legend(loc = "lower right")
    plt.xlabel("iterations")
    plt.ylabel("root p")
    plt.show()


if __name__ == '__main__':
    main()
