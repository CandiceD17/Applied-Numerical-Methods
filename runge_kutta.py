import numpy as np
import matplotlib.pyplot as plt
import math


def y(x):
    return 1 / 5 * x * math.exp(3 * x) - 1 / 25 * math.exp(3 * x) + 1 / 25 * math.exp(-2 * x)


def f(t, w):
    # return t * math.exp(3 * t) - 2 * w
    return (w / t) ** 2 + w / t


def plot(x, w, method):
    xs = np.linspace(0, 1, 100)
    ys = [y(x) for x in xs]
    x = x
    w = w
    plt.plot(xs, ys, label="actual_solution")
    plt.plot(x, w, label=method)
    plt.legend(loc="upper left")
    plt.show()


def runge_kutta(a, b, h, w0):
    ws = [w0]
    for i in range(1, int((b - a)/h) + 1):
        w = ws[-1]
        t_prev = h * (i - 1)
        t_i = h * i
        k_1 = h * f(t_prev, w)
        k_2 = h * f(t_prev + 0.5 * h, w + 1/2 * k_1)
        k_3 = h * f(t_prev + 0.5 * h, w + 1/2 * k_2)
        k_4 = h * f(t_i, w + k_3)
        ks = [k_1, k_2, k_3, k_4]
        print(ks)
        w = w + 1 / 6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        ws.append(w)
    print(ws)


def runge_kutta_fehlberg(a, b, w0, h_min, h_max, tol):
    ts = [a]
    ws = [w0]
    t = a
    w = w0
    h = h_max
    flag = 1
    print([t, w, h])
    while flag == 1:
        k1 = h * f(t, w)
        k2 = h * f(t + 1/4 * h, w + 1/4 * k1)
        k3 = h * f(t + 3/8 * h, w + 3/32 * k1 + 9/32 * k2)
        k4 = h * f(t + 12/13 * h, w + 1932/2197 * k1 - 7200/2197 * k2 + 7296/2197 * k3)
        k5 = h * f(t + h, w + 439/216 * k1 - 8 * k2 + 3680/513 * k3 - 845/4104 * k4)
        k6 = h * f(t + 1/2 * h, w - 8/27 * k1 + 2 * k2 - 3544/2565 * k3 + 1859/4104 * k4 - 11/40 * k5)
        r = 1 / h * np.abs(1/360 * k1 - 128/4275 * k3 - 2197/75240 * k4 + 1/50 * k5 + 2/55 * k6)
        if r <= tol:
            t = t + h
            w = w + 25/216 * k1 + 1408/2565 * k3 + 2197/4104 * k4 - 1/5 * k5
            ts.append(t)
            ws.append(w)
            print([round(t, 2), w, round(h, 2)])
        sigma = 0.84 * (tol / r) ** (1/4)
        if sigma <= 0.1:
            h = 0.1 * h
        elif sigma >= 4:
            h = 4 * h
        else:
            h = sigma * h
        if h > h_max:
            h = h_max
        if t >= b:
            flag = 0
        elif t + h > b:
            h = b - t
        elif h < h_min:
            flag = 0
            print('minimum h exceeded')
    return ts, ws


def main():
    # runge_kutta(0, 1, 0.5, 0)
    t, w = runge_kutta_fehlberg(1, 1.2, 1, 0.02, 0.05, 1e-4)
    plot(t, w, "runge_kutta_fehlberg")


if __name__ == '__main__':
    main()
