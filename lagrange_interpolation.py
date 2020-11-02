import math
import matplotlib.pyplot as plt
import numpy as np
import pdb


def f(x):
    return 1/(1 + pow(x, 2))


def lagrange(xs, x_eval):
    res = 0
    for i in range(len(xs)):
        prod = f(xs[i])
        for j in range(len(xs)):
            if i != j:
                prod *= (x_eval - xs[j]) / (xs[i] - xs[j])
        res += prod
    return res


def equally_x(n):
    interval = 10/n
    xs = [-5]
    for i in range(n):
        xs.append(xs[-1] + interval)
    return xs


def chebyshev_x(n):
    xs = []
    for i in range(n+1):
        xs.append(-5 * math.cos((2 * i + 1)/(2 * n + 2) * math.pi))
    return xs


def main():
    x_evals = np.linspace(-5, 5, 100)
    ns = [5, 10, 25, 50]
    ys = []
    ys_1 = [[0], [0], [0], [0]]
    ys_2 = [[0], [0], [0], [0]]
    err_1 = [[0], [0], [0], [0]]
    err_2 = [[0], [0], [0], [0]]
    index = 0

    for n in ns:
        xs_1 = equally_x(n)
        xs_2 = chebyshev_x(n)
        for x_eval in x_evals:
            eval_1 = lagrange(xs_1, x_eval)
            eval_2 = lagrange(xs_2, x_eval)
            y = f(x_eval)
            ys_1[index].append(eval_1)
            ys_2[index].append(eval_2)
            err_1[index].append(abs(y-eval_1))
            err_2[index].append(abs(y-eval_2))
        ys_1[index] = ys_1[index][1:]
        ys_2[index] = ys_2[index][1:]
        err_1[index] = err_1[index][1:]
        err_2[index] = err_2[index][1:]
        index += 1

    for x_eval in x_evals:
        y = f(x_eval)
        ys.append(y)

    figure, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x_evals, ys_1[0], label = "p(x), n = 5")
    axs[0, 0].plot(x_evals, ys_1[1], label = "p(x), n = 10")
    axs[0, 0].plot(x_evals, ys_1[2], label = "p(x), n = 25")
    axs[0, 0].plot(x_evals, ys_1[3], label = "p(x), n = 50")
    axs[0, 0].plot(x_evals, ys, label = "f(x)")
    axs[0, 0].set_ylim((-5, 5))
    axs[0, 0].legend(loc = "upper left")

    axs[0, 1].plot(x_evals, err_1[0], label = "e(x), n = 5")
    axs[0, 1].plot(x_evals, err_1[1], label = "e(x), n = 10")
    axs[0, 1].plot(x_evals, err_1[2], label = "e(x), n = 25")
    axs[0, 1].plot(x_evals, err_1[3], label = "e(x), n = 50")
    axs[0, 1].set_ylim((0, 10))
    axs[0, 1].legend(loc = "upper left")

    axs[1, 0].plot(x_evals, ys_2[0], label="p(x), n = 5")
    axs[1, 0].plot(x_evals, ys_2[1], label="p(x), n = 10")
    axs[1, 0].plot(x_evals, ys_2[2], label="p(x), n = 25")
    axs[1, 0].plot(x_evals, ys_2[3], label="p(x), n = 50")
    axs[1, 0].plot(x_evals, ys, label="f(x)")
    axs[1, 0].legend(loc="upper left")

    axs[1, 1].plot(x_evals, err_2[0], label="e(x), n = 5")
    axs[1, 1].plot(x_evals, err_2[1], label="e(x), n = 10")
    axs[1, 1].plot(x_evals, err_2[2], label="e(x), n = 25")
    axs[1, 1].plot(x_evals, err_2[3], label="e(x), n = 50")
    axs[1, 1].legend(loc="upper left")

    plt.show()




if __name__ == '__main__':
    main()
