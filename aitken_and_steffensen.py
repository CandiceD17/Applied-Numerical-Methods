import math
import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return 1 + math.exp(-x)

def fixed_point(p0, tol, maxIter):
    p = p0
    ps = [p0]
    for i in range(maxIter):
        p = g(p)
        if abs(g(p) - p) < tol:
            ps.append(p)
            return p, ps
        ps.append(p)
    return p, ps


def aitken(p0, tol, maxIter):
    p = p0
    p_fp = p0
    ps = []
    ps_fp = [p0]
    for i in range(maxIter):
        p_fp = g(p_fp)
        ps_fp.append(p_fp)
        if i >= 1:
            p = ps_fp[-3] - pow(ps_fp[-2] - ps_fp[-3], 2) / (ps_fp[-1] - 2 * ps_fp[-2] + ps_fp[-3])
            if abs(g(p) - p) < tol:
                ps.append(p)
                return p, ps
            ps.append(p)
    return p, ps


def steffensen(p0, tol, maxIter):
    ps = [p0]
    p_level = [p0, g(p0), g(g(p0))]
    for i in range(maxIter):
        p_level[0] = p_level[0] - pow(p_level[1] - p_level[0], 2) / (p_level[2] - 2 * p_level[1] + p_level[0])
        p_level[1] = g(p_level[0])
        p_level[2] = g(p_level[1])
        if abs(g(p_level[0]) - p_level[0]) < tol:
            ps.append(p_level[0])
            return p_level[0], ps
        ps.append(p_level[0])
    return p_level[0], ps


def main():
    p_fp, ps_fp = fixed_point(1, 1e-5, 100)
    print(ps_fp)
    p_ak, ps_ak = aitken(1, 1e-5, 100)
    p_sf, ps_sf = steffensen(1, 1e-5, 100)
    index_fp = [i for i in range(len(ps_fp))]
    index_ak = [i for i in range(len(ps_ak))]
    index_sf = [i for i in range(len(ps_sf))]
    plt.plot(index_fp, ps_fp, label = "fixed point iteration")
    plt.plot(index_ak, ps_ak, label = "Aitken's method")
    plt.plot(index_sf, ps_sf, label = "Steffensen's method")
    plt.legend(loc = "lower right")
    plt.xlabel("iterations")
    plt.ylabel('p value')
    plt.show()


if __name__ == '__main__':
    main()
