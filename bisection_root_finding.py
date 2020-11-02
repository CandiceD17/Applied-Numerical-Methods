import math
import numpy as np
import matplotlib.pyplot as plt


def sign(x):
    if x < 0:
        return -1
    else:
        return 1


# returns the result of f = x^2 - 0.7*x for problem 3
# or f = sqrt(x) - cos(x) for problem 4
def func(x, problem):
    if problem == 3:
        return pow(x, 2) - 0.7 * x
    elif problem == 4:
        return math.sqrt(x) - math.cos(x)


# the bisection algorithm
# input: initial bound [a, b], number of iterations, and problem number (3 or 4)
def bisection(a, b, iters, problem):
    fA = func(a, problem)
    fB = func(b, problem)
    if iters < 1:
        print("Error: iterations must be >= 1.\n")
        return
    elif a >= b:
        print("Error: a is not less than b.\n")
        return
    elif fA == 0 or fB == 0:
        print("Error: zero value: f(a) = %f, f(b) = %f\n", fA, fB)
        return
    elif fA * fB > 0:
        print("Error: same signs")
        return

    ps = []  # an array to store the past results
    for i in range(iters):
        mid = (a + b) / 2
        fMid = func(mid, problem)
        fA = func(a, problem)
        ps.append(mid)
        if sign(fMid) == sign(fA):
            a = mid
        else:
            b = mid
    root = mid
    return root, ps


def graph(p, ps, problem):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    y1 = [abs(v - p) for v in ps]  # calculate |p_n - p| for every n
    y2 = []
    y3 = [abs(func(v, problem)) for v in ps]  # calculate |f(p_n)| for every n
    for i in range(len(ps)-1):
        y2.append(abs(ps[i+1]-ps[i]))  # calculate |p_n+1 - p_n| for every n
    x1 = np.arange(1, len(ps) + 1)  # create an array from 1 to # of iterations + 1
    x2 = np.arange(1, len(ps))
    ax1.plot(x1, y1)
    ax1.set(xlabel='iterations', ylabel='|p_n - p|')
    ax2.plot(x2, y2)
    ax2.set(xlabel='iterations', ylabel='|p_n+1 - p_n|')
    ax3.plot(x1, y3)
    ax3.set(xlabel='iterations', ylabel='f(|p_n|)')

    plt.show()


def main():
    # this is calling bisection for problem 4
    root, ps = bisection(0, 1, 20, 4)
    graph(root, ps, 4)
    print(root)


if __name__ == '__main__':
    main()
