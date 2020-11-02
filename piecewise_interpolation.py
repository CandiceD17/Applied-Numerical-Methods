import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.exp(-2 * x) + 2 * pow(x, 2) + x + 1


def generate_x(n):
    interval = 1/n
    xs = [0]
    for i in range(n):
        xs.append(xs[-1] + interval)
    return xs


def piecewise_p(x0, x1, x_eval):
    a = f(x1)
    b = (f(x1) - f(x0)) / (x1 - x0)
    return a + b * (x_eval - x1)


def main():
    x_evals = np.linspace(0, 1, 1000)
    n = 317
    xs = generate_x(n)
    ys = []
    y_pred = []
    error = []
    index = 0
    for x_eval in x_evals:
        if index + 1 < n and x_eval >= xs[index + 1]:
            index = index + 1
        f_val = f(x_eval)
        f_pred = piecewise_p(xs[index], xs[index + 1], x_eval)
        ys.append(f_val)
        y_pred.append(f_pred)
        error.append(abs(f_val-f_pred))

    plt.plot(x_evals, ys, label = "f(x)")
    plt.plot(x_evals, y_pred, '--', label = "piecewise approximation")
    plt.legend(loc = "upper left")
    plt.show()

    print(max(error))

if __name__ == '__main__':
    main()
