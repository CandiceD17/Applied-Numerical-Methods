import math
import matplotlib.pyplot as plt
import numpy as np


def y_sol(t):
    return t ** 2 * (math.exp(t) - math.exp(1))


def euler_estimate(wi, ti):
    return wi + 0.1 * (2 / ti * wi + ti ** 2 * math.exp(ti))


def linear_interpolation(t1, w1, t2, w2, t):
    slope = (w2 - w1) / (t2 - t1)
    intercept = w1 - slope * t1
    return slope * t + intercept


def part_a():
    res = []
    wi = 0
    ti = 1
    ws = [wi]
    for i in range(1, 11):
        wi = euler_estimate(wi, ti)
        ws.append(wi)
        ti = round(1 + 0.1 * i, 1)
        out = [ti, wi]
        yi = y_sol(ti)
        out.append(yi)
        out.append(abs(yi - wi))
        res.append(out)
    for row in res:
        print(row)
    return ws


def part_b(ws):
    res = []
    w1 = linear_interpolation(1, ws[0], 1.1, ws[1], 1.04)
    y1 = y_sol(1.04)
    res.append([1.04, w1, y1, abs(y1 - w1)])
    w1 = linear_interpolation(1.5, ws[5], 1.6, ws[6], 1.55)
    y1 = y_sol(1.55)
    res.append([1.55, w1, y1, abs(y1 - w1)])
    w1 = linear_interpolation(1.9, ws[9], 2, ws[10], 1.97)
    y1 = y_sol(1.97)
    res.append([1.97, w1, y1, abs(y1 - w1)])
    for row in res:
        print(row)


def main():
    ws = part_a()
    part_b(ws)
    t_eval = np.linspace(1, 2, 100)
    ys = [y_sol(t) for t in t_eval]
    t_plot = [1 + 0.1 * i for i in range(0, 11)]
    plt.plot(t_eval, ys, label = "actual_y")
    plt.plot(t_plot, ws, label = "Euler_approx")
    plt.legend(loc="upper left")
    plt.show()


if __name__ == '__main__':
    main()
